css_sheet ="""
    <style>
    /* Main Page Background with Image */


    /* Style for Column 1 (Fixed Position) */
    
    .fixed-col {
        position: fixed;
        top: 0;
        left: 0;
        width: 20%; /* Adjust width as needed */
        height: 100%;
        background-color: #FFDDC1; /* Light peach */
        padding: 20px;
        border-right: 2px solid #CCCCCC; /* Optional: Divider line */
        box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.1);
        overflow-y: auto; /* Allow scrolling within this column */
    }

    /* Style for Column 2 */
    .col2 {
        background-color: #041527;  /* Light green */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }


    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color:#041527;
        position: sticky;
        top: 0;  /* Keeps it at the top when you scroll */
        width: 350px;
        height: 100vh;  /* Make the sidebar take full height of the viewport */
        padding: 20px;
        color: white;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);  /* Optional: shadow to give depth */

    }
    
    /* Main page background */
    .main {
        background-color:#F4F2EE;
        color:black;
    }
    
    
    /* Sidebar text color and font */
    [data-testid="stSidebar"] * {
        
        color: #E0E0E0;  /* Light gray for readability */
        font-family: 'Roboto', sans-serif;  /* Modern font */
        h1, h2, h3, h4, h5, h6 {
        color: #4577bc;
    }
    }
    
    
    
    /* Hover effect for navigation links */
    .nav-links a:hover {
        background-color: #E0E0E0;
        color: white;
    }
    
    
    /* Navigation Links */
    .nav-links a {
        display: block;
        padding: 10px;
        color: #8A2BE2;
        text-decoration: none;
        margin-bottom: 10px;
    }
    
     /* Navigation Sidebar Styling */
    .navigation-sidebar {
        background-color: #2a2e3f;
        padding: 10px;
        color: #E0E0E0;
        text-align: left;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        width: 250px;
    }
    
    
    /* Profile image styling (circular cut-out and centered) */
    .sidebar-profile-img {
        width: 210px;
        height: 210px;
        object-fit: cover;
        border-radius: 60%;
        border: 3px dashed #4577bc;  /* Optional border around the image */
        margin-bottom: 20px;
        
        position: sticky;
        top: 0;  /* Keeps it at the top when you scroll */
        padding: 20px;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);  /* Optional: shadow to give depth */
    }


    /* Customize headings */
    h1, h2, h3, h4, h5, h6 {
        color: #4577bc;
    }

    /* Links */
    a {
        color: #8A2BE2;  /* Example for hyperlink color */
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    </style>
    
    
 
    """
    
    
    
    
#best colors  #042027