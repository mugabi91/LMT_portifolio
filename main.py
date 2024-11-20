
############### start of imports ################################################################################################
from views import *
from css import css_sheet
                
# START OF MAIN FUNCTION
def main():            
    df: pd.DataFrame | None = read_file(starwars_data_location)
    if df is None:
        st.write(f">>>[Error Info]:File type unsupported. No DATA loaded") #type: ignore
        
    rows_in_data = df.shape[0] # type:ignore
    cols_in_data = df.shape[1] # type:ignore
    
    st.set_page_config(page_title="LMT Portfolio", layout="wide", initial_sidebar_state="expanded",page_icon=my_logo_pic)
  
    # pages style 
    st.markdown(css_sheet, unsafe_allow_html=True)

    # sidebar area
    with st.sidebar:
        # sidebar title
        st.sidebar.title("Profile")
        st.markdown(f"<img class='sidebar-profile-img' src='{ my_logo_pic }'/>", unsafe_allow_html=True)
        
        # about me section
        st.sidebar.subheader("About Me")
        st.sidebar.write(profile_intro) #type:ignore

        # Skills Section
        st.sidebar.subheader("Skills")
        st.sidebar.write(skill_listing) #type:ignore
        
        #contact section 

        st.sidebar.markdown(
            """
            <div>
                <h3>Contact Me</h3>
                <p>Email: <a href="mailto:Trevortravis91+porti@gmail.com?subject=Contact from Your Portfolio&body=Hi, I would like to get in touch with you regarding...">Trevortravis91+porti@gmail.com</a></p>
                <p>LinkedIn: <a href="https://www.linkedin.com/in/mugabi-trevor" target="_blank">Mugabi Trevor</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )
                
    

    ### page one start
    col2, col1 = st.columns([5,1])
    
    with col1:
        st.subheader("To Go")
        page = st.radio("Page", options=(
            page_one_name, 
            page_two_name,
            page_three_name
    )   
)       
    
        
    with col2:
        # Add the "Return to Top" button with smooth scroll functionality

        if page == page_one_name:
            st.markdown("<div class=col2><div>",unsafe_allow_html=True)
            page_one_view(rows_in_data,cols_in_data,df) #type: ignore
            st.markdown("<div class=col2><div>",unsafe_allow_html=True)
            page_one_view_extension(df) #type: ignore
            st.markdown("<div class=col2><div>",unsafe_allow_html=True)
            
        
        ## page two start 
        elif page == page_two_name:
            st.markdown("<div class=col2><div>",unsafe_allow_html=True)
            page_two_view()
            
            

        elif page == page_three_name:
            st.markdown("<div class=col2><div>",unsafe_allow_html=True)
            page_three_view()
            st.markdown("<div class=col2><div>",unsafe_allow_html=True)
            

if __name__ == "__main__":
    main()





#