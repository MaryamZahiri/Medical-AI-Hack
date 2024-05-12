'''
Med AI Web Server
'''
from flask import Flask, render_template, request, Response
from parse_pdf import extract_text_from_pdf
from gpt_agent import gpt_agent
import mediapipe as mp
import time
import cv2
import os
import json

app = Flask(__name__)



def apply_overlay(video_path):
    # Initialize pose estimator
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Open video file
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_width = 1920
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_height = 1080
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = 30

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video_path = 'static/videos/output.mp4'
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # Process each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process the frame for pose detection
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pose_results = pose.process(frame_rgb)
        mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Write the frame with overlay to the output video
        out.write(frame)

    # Release video capture and writer objects
    cap.release()
    out.release()

    return output_video_path

def generate_frames_seam(video_path, speed_multiplier=1.0):

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Open video file
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #frame_width = 1920
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #frame_height = 1080
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = 30

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video_path = 'static/videos/Calories_pose.mp4'
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # org 
    org = (100,200) 
    
    # fontScale 
    fontScale = 5
    
    # Blue color in BGR 
    color = (255, 255, 255) 
    
    # Line thickness of 2 px 
    thickness = 3

    i=0
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)
    actions=['walking']*(length//10)+['running']*(length//14) + ['jumping']*(length//12)+['running']*(length//8)+['stretch']*(length//3)
   
    # Process each frame of the video
    while cap.isOpened() or i<len(actions):
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process the frame for pose detection
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pose_results = pose.process(frame_rgb)
        mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Write the frame with overlay to the output video
        out.write(frame)

        # Using cv2.putText() method 
        image = cv2.putText(frame, actions[i], org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 


        _, buffer = cv2.imencode('.jpg', image)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.01)
        i+=1
       



########################## All headers ################################################
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/lab-report')
def lab_report():
    return render_template('/header_html/lab_report.html')

@app.route('/calories-tracker')
def calory_tracker():
    return render_template('/header_html/calories_tracker.html')


@app.route('/upload_seam', methods=['POST'])
def upload_seam():
    global last_uploaded_video_path_seam
    if 'video' not in request.files:
        return "No file part"
    file = request.files['video']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = "uploaded_video.mp4"
        file_path = os.path.join('static/videos', filename)
        file.save(file_path)
        last_uploaded_video_path_seam = file_path
        return render_template('header_html/calories_tracker.html', video_name=filename)
    return "Invalid file type"


# Declare a variable to store the last uploaded video path
last_uploaded_video_path_seam, last_uploaded_video_path_defect = None, None

@app.route('/video_feed_seam')
def video_feed_seam():
    global last_uploaded_video_path_seam
    return Response(generate_frames_seam(last_uploaded_video_path_seam),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/symptom-tracker')
def symptom_tracker():
    return render_template('/header_html/symptom_tracker.html')

@app.route('/dashboard')
def dashboard():
    return render_template('/header_html/dashboard.html')

@app.route('/join')
def join():
    return render_template('/header_html/join.html')

# @app.route('/chat-bot')
# def chat_bot():
#     return render_template('/header_html/chat_bot.html')

# @app.route('/testimonial')
# def chat_bot():
#     return render_template('/header_html/testimonial.html')

@app.route('/testimonial')
def testimonial():
    with open('static/testimonials.json', 'r') as f:
        testimonials = json.load(f)
    return render_template('header_html/testimonial.html', testimonials=testimonials)

##################################### first page #########################################
@app.route('/upload', methods=['POST'])
def upload():
    if 'pdfFile' not in request.files:
        return 'No file part'

    file = request.files['pdfFile']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the uploaded file to a temporary location
        file.save('temp.pdf')

        extracted_text = extract_text_from_pdf("temp.pdf")

        # print(extracted_text)
        # # Return the extracted text to the client
        extracted_text_analyse = gpt_agent(extracted_text)

        return f"The Extracted text is as follows:\n{extracted_text_analyse}\n"

    return 'File uploaded successfully'

if __name__== '__main__':
    app.run(port=8000, host='0.0.0.0', debug=True)