const med_ai_footer_template = document.createElement('template');
med_ai_footer_template.innerHTML = `
    <!-- Google fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <!-- Window tab icon -->
    <link rel="icon" href="static/images/webicon.png" type="images/x-icon">
    
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        :root {
            --primary-color:#93C572;
            --light-color: #f4f4f6;
            --dark-color: #111;
        }

        /* Links */
        a {
            text-decoration: none;
            color: #331
        }

        /* List */
            li {
            list-style: none;
        }

        img {
            max-width: 100%;
        }

        /* Footer */
        .footer {
            position: relative;
            bottom: 0;
            width: 100%;
            background-color: #333; /* Adjust as needed */
            color: #fff; /* Adjust as needed */
            padding: 20px 0; /* Adjust as needed */
            text-align: center; /* Adjust as needed */
        }

        .footer .footer-logo {
            justify-content: center;
            position: center;
        }
        .footer .footer-logo .logo {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .footer .footer-media {
            justify-content: center;
            align-items: center;
        }

        .footer i {
            font-size: 1rem;
            margin-right: 10px;
            
        }

        .footer .h4 {
            margin-bottom: 10px;
        }

        .footer ul li {
            line-height: 2.5;
        }

        .footer a {
            color: #ccc;
        }

        .footer .logo {
            width: 100px;
            height: 70px;
        }

        .footer .footer-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
        }

        /* Utility Classes */
        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 15px
        }

        /* Buttons */
        .btn {
            display: inline-block;
            padding: 13px 20px;
            background: var(--light-color);
            color: #333;
            font-weight: 600;
            text-decoration: none;
            text-align: center;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.5s;
        }

        .btn:hover {
            opacity: 0.8;
        }

        /* Background */
        .background-dark {
            background: var(--dark-color);
            /* Text color */
            color: #fff;
        }
    </style>

    <footer class="footer background-dark">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-logo">
                    <a class="logo" href="/lab-report">
                        <img src="static/images/logo.PNG" alt="logo">
                    </a>
                    <!-- <div class="card"></div> -->
                    <div class="footer-media">
                        <i class="fab fa-linkedin"></i>
                        <i class="fab fa-github"></i>
                    </div>
                </div>
                <div>
                    <h4>Company</h4>
                    <ul>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Our future Work</a></li>
                        <li><a href="#">Our Team</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="#">News</a></li>
                        <li><a href="#">Research</a></li>
                        <li><a href="#">Recent Project</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Prices</h4>
                    <ul>
                        <li><a href="#">Pricing</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="#">medai.com</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
`;

class MedAiFooter extends HTMLElement {

  constructor() {
    super();    
    
    this.attachShadow({ mode: 'open'});
    this.shadowRoot.appendChild(med_ai_footer_template.content.cloneNode(true));
  }

  connectedCallback() {
  }

  disconnectedCallback() {
  }
}

window.customElements.define('med-ai-footer', MedAiFooter);