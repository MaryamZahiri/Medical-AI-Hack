const med_ai_header_template = document.createElement('template');
med_ai_header_template.innerHTML = `
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
        .navbar {
            background-color: #90EE90;
            padding: 20px;
        }

        .navbar .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .navbar .logo {
            width: 100px;
            height: 70px;
        }

        .navbar .main-menu .tab-header {
            display: flex;
        }

        .navbar .tab-header li a {
            padding: 10px 20px;
            display: block;
            font-weight: 600;
            transition: 0.5s;
        }

        .navbar .tab-header li a:hover {
            color: var(--primary-color);
        }

        .navbar .tab-header li a i {
            margin-right: 10px;
        }

        .navbar .tab-header li:last-child a {
            margin-left: 10px;
        }

        /* Utility Classes */
        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 15px
        }

        /* Text Classes */
        /* relative to root font size: 16px */
        .text-xxl {
            font-size: 3rem;
            line-height: 1.2;
            font-weight: 600;
            margin: 40px 0 20px;
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

        /* Hamburger Button */
        .hamburger-button {
            display: none;
            background: none;
            border: none;
            cursor: pointer;
            padding: 10px;
            z-index: 1000;
        }

        .hamburger-button .hamburger-line {
            width: 30px;
            height: 3px;
            background: #333;
            margin: 6px 0;
        }

        /* Mobile Menu */
        .mobile-menu {
            position: fixed;
            top: 0;
            /* right: 0; */
            right: -300px;
            width: 250px;
            height: 100%;
            z-index: 100;
            background: #fff;
            box-shadow: 0px 0px 10px rgb(0,0,0,0.2);
            transition: right 0.3s ease-in-out;
        }

        .mobile-menu.active {
            right: 0;
        }
        .mobile-menu ul {
            margin-top: 30px;
            padding-right: 10px;
        }

        .mobile-menu ul li {
            margin: 10px 0;
        }

        .mobile-menu ul li a {
            font-size: 12px;
            transition: 0.3s;
        }

        .hidden {
            right: -300px;
        }

        /* Media Queries */
        @media (max-width: 960px) {
            .text-xxl {
                font-size: 2.5rem;
            }
        }

        @media (max-width: 670px) {
            .navbar .main-menu {
                display: none;
            }

            .navbar .hamburger-button {
                display: block;
            }
        }

        @media (max-width: 500px) {

        }
    </style>

    <div class="navbar">
        <div class="container">
            <div class="logo">
                <a href="/">
                    <img src="static/images/logo.PNG" alt="logo">
                </a>
            </div>
            <div class="main-menu">
                <ul class="tab-header">
                    <li><a href="/lab-report">Lab Report</a></li>
                    <li><a href="/calories-tracker">Calories Tracker</a></li>
                    <li><a href="/symptom-tracker">AI Symptom Tracker</a></li>
                    <li><a href="/dashboard">Dashboard</a></li>
                    <li><a href="/testimonial">Testimonials</a></li>
                    <li><a href="join">Join us</a></li>
                    <!-- <li><a class="btn" href="/chat-bot">
                        <i class="fas fa-user"></i> Chat Bot
                    </a></li> -->
                </ul>
            </div>

            <div id="hamburger-button" class="hamburger-button">
                <div class="hamburger-line"></div>
                <div class="hamburger-line"></div>
                <div class="hamburger-line"></div>
            </div>
            <div class="mobile-menu">
                <ul class="tab-header">
                    <li><a href="/lab-report">Lab Report</a></li>
                    <li><a href="/calories-tracker">Calories Tracker</a></li>
                    <li><a href="/symptom-tracker">AI Symptom Tracker</a></li>
                    <li><a href="/dashboard">Dashboard</a></li>
                    <li><a href="/join">Join us</a></li>
                    <li><a class="btn" href="/chat-bot">
                        <!-- i tag icon -->
                        <i class="fas fa-user"></i> Chat Bot
                    </a></li>
                </ul>
            </div>

        </div>
    </div>
`;

class MedAiHeader extends HTMLElement {

    constructor() {
        super();    
        this.updateView = this.updateView.bind(this);
        this.toggleBlockMods = this.toggleBlockMods.bind(this); // Bind the method to ensure it has the correct context
        this.toggleMobileMenuVisibility = this.toggleMobileMenuVisibility.bind(this);


        this.attachShadow({ mode: 'open'});
        this.shadowRoot.appendChild(med_ai_header_template.content.cloneNode(true));
    }

    connectedCallback() {
        this.updateView();
        this.toggleBlockMods();
        this.toggleMobileMenuVisibility();

        this.shadowRoot.querySelector('.hamburger-button')
       .addEventListener('click', this.toggleBlockMods); // Use the bound method here
       window.addEventListener('resize', this.toggleMobileMenuVisibility);
    }

    disconnectedCallback() {
        this.shadowRoot.querySelector('.hamburger-button')
        .removeEventListener('click', this.toggleBlockMods); // Use the bound method here
        window.removeEventListener('resize', this.toggleMobileMenuVisibility);
    }

    toggleBlockMods() {
        const mobileMenu = this.shadowRoot.querySelector('.mobile-menu');
        if (mobileMenu.classList.contains('active')) {
            mobileMenu.classList.remove('active');
        } else {
            mobileMenu.classList.add('active');
        }
    }

    toggleMobileMenuVisibility() {
        const mobileMenu = this.shadowRoot.querySelector('.mobile-menu');
        if (window.innerWidth > 670) {
            mobileMenu.classList.remove('active');
        } 
        // else {
        //     mobileMenu.classList.add('active');
        // }
    }

    updateView() {
        // Your existing updateView method implementation
    }
}

window.customElements.define('med-ai-header', MedAiHeader);