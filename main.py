
############### start of imports ################################################################################################
from views import *
                
# START OF MAIN FUNCTION
def main():            
    df: pd.DataFrame | None = read_file(starwars_data_location)
    if df is None:
        st.write(f">>>[Error Info]:File type unsupported. No DATA loaded") #type: ignore
        
    rows_in_data = df.shape[0] # type:ignore
    cols_in_data = df.shape[1] # type:ignore
    st.set_page_config(layout="wide") 
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to", (page_one_name, page_two_name))
        
    ### page one start
    if page == page_one_name: 
        page_one_view(rows_in_data,cols_in_data,df) #type: ignore
        page_one_view_extension(df) #type: ignore
        
    ## page two start 
    elif page == page_two_name:
        st.write(""" # Under Construction.. 
        if Rome was constructed in one day!, we would use the same contractors.""") #type: ignore
    
        


main()





#