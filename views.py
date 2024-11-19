import pandas as pd 
import streamlit as st 
import time 
from image_urls import *
from contents import *
import plotly.express as px #type: ignore
import numpy as np 
from PIL import Image # type:ignore
import matplotlib.pyplot as plt #type: ignore

# start of helper functions..

#function to create type write effect
def stream_data(body:str):
    for word in body.split(" "):
        yield word + " "
        time.sleep(0.02)


# function to read datasets
def read_file(file_location:str):
    supported_file_types: list[str] =[
    ".xlsx",  # Excel Workbook (XML-based)
    ".xlsm",  # Excel Macro-Enabled Workbook (XML-based)
    ".xls",   # Excel 97-2003 Workbook (Binary-based)
    ".csv",   # Comma Separated Values
    ".xltx",  # Excel Template (XML-based)
    ".xltm",  # Excel Macro-Enabled Template (XML-based)
    ".xlsb",  # Excel Binary Workbook
    ".ods"    # OpenDocument Spreadsheet
]

    file_type: str = file_location.split(".")[-1].lower()
    if file_type in supported_file_types:
        df: pd.DataFrame = pd.read_excel(file_location) # type: ignore
        return df 
    else:
        match file_type:
            case "csv":
                df = pd.read_csv(file_location) # type: ignore
                return df 
            case "json":
                df = pd.read_json(file_location) # type: ignore
                return df

            case "parquet":
                df = pd.read_parquet(file_location) 
            case _ :
                print(f">>>[Error Info]:File type unsupported..")
                return None


# end of helper funcs




# page one view 
def page_one_view(rows_in_data:int,cols_in_data:int):
    #title 
    st.write(page_one_title.upper()) #type: ignore
    
    #BIO
    st.write(bio) #type: ignore
    
    #intro of page
    st.image(vaders_starwars_pic, caption=caption_vaders_pic)
    st.write_stream(stream_data(intro))
    st.write(dataset_subtitle.capitalize()) #type: ignore
    time.sleep(0.2)
    st.dataframe(df, use_container_width=True) #type: ignore
    st.write_stream(stream_data(f"Dataset holds {rows_in_data} rows and {cols_in_data} columns"))
    st.write_stream(stream_data(startrek_subtitle))
    st.image(startrek_pic,caption=caption_startrek_pic)
    
    st.write_stream(stream_data(startrek_bio))
    
    st.divider()

def page_two_view():
    st.write(page_2_title)  #type: ignore
    
    # Load the image
    image = Image.open(glob_image_location)  # type:ignore
    # Resize the image
    max_width = 1800  # Maximum width for display
    if image.width > max_width: # type:ignore
        aspect_ratio = image.height / image.width # type:ignore 
        new_width = max_width 
        new_height = int(max_width * aspect_ratio) # type:ignore
        image = image.resize((new_width, new_height)) # type:ignore

# Display the resized image
    st.image(image, caption='image', use_column_width=True) # type:ignore

    df.drop_duplicates() # type: ignore
    
    df.drop(drop_columns,axis=1,inplace=True)  # type: ignore

    ro, wi = df.shape # type: ignore
    total_slots = ro*wi # type: ignore
    

    df.rename(columns=rename_columns_dict, inplace=True) #type: ignore
    
    st.divider()
    
    st.write_stream(stream_data(""" #### Data cleaning:
            My Process
            Dropped the useless variables
            Dropped the duplicated entries
            Renamed the long Variable names as below 
            Did data type convertions
            Did some exploring after
            
            """))
    
    variable_names = pd.DataFrame(list(rename_columns_dict.items()), columns=['OLD VARiABLE NAME', 'NEW VARIABLE NAME'])
    time.sleep(0.2)
    
    st.dataframe(variable_names) # type: ignore
    st.divider()
    total_nulls = df.isna().sum().reset_index() # type: ignore 
    total_nulls.columns = ['Variable','Null_total']
    loss_percentage =  (np.sum(total_nulls["Null_total"])/total_slots)*100 # type: ignore

    st.divider()
    
    st.write_stream(stream_data(null_number_title))
    
    time.sleep(0.2)
    
    st.dataframe(total_nulls) # type:ignore
    
    st.write_stream(stream_data(f"{loss_percentage:.2f}% of the data will be lost if all nulls are dropped"))

    st.divider()
    st.write_stream(stream_data(observation_title))
    st.divider()
    st.write_stream(stream_data('''#### What is the make up of the fans by franchise ?'''))
    
    
    

    columns = [feature for feature in df.columns if feature != "RespondentID"]  # type: ignore
    

    df.drop(df[df['RespondentID'].isna()].index, inplace=True) # type: ignore
    df.reset_index(drop=True,inplace=True) # type: ignore
    df['RespondentID'] = pd.to_numeric(df['RespondentID'],errors="coerce") # type: ignore
    df['RespondentID'] = df['RespondentID'].astype(object) # type: ignore
    
    
    for col in columns: # type: ignore
        df[col] = df[col].astype("category") # type: ignore
        
    #df.info() # type: ignore

    categories = ['starwars_fan', 'star_trek_fan', 'Expanded_universe_fan']
    titles = ['Number of Star Wars fans', 'Number of Star Trek fans', 'Number of Expanded Universe fans']

    
    gender_count = df.groupby('Gender',observed=False).agg( #type: ignore
        starwars_fan=('starwars_fan', 'count'), 
        star_trek_fan=('star_trek_fan', 'count'),
        Expanded_universe_fan=("Expanded_universe_fan","count"),
        Count=('Location', 'size')
        ).reset_index() # type: ignore
    gender_count # type: ignore
    
    
    # Melt the DataFrame to have a single 'Count' column for visualization
    melted_df = pd.melt(  #type: ignore
        gender_count,  # type: ignore
        id_vars=['Gender', 'Count'], 
        var_name='Category', 
        value_name='Value'
        ) # type: ignore
    
    # Create a grouped bar chart using Plotly Express
    fi1g = px.bar(  #type: ignore
        melted_df, 
        x='Gender', 
        y='Value',
        color='Category',
        barmode='group',
        hover_data={'Value': ':.0f'}, labels={'Value': 'Count'},
        title='Counts by Gender and Fan Categories'
        )
    
    # Update layout and show the plot
    fi1g.update_layout(  #type: ignore
        xaxis_title='Gender',
        yaxis_title='Count', 
        legend_title='Category',
        width=1000, height=500
    )
    #fi1g.show() # type: ignore
    st.plotly_chart(fi1g) # type: ignore





    fan_Age_count = df.groupby('Age',observed=False).agg( # type: ignore
        starwars_fan=('starwars_fan', 'count'),
        star_trek_fan=('star_trek_fan', 'count'), 
        Expanded_universe_fan=("Expanded_universe_fan","count"),
        Count=('Location', 'size')
        ).reset_index() # type: ignore
    
    
    

    # Melt the DataFrame to have a single 'Count' column for visualization
    melted_df = pd.melt( # type: ignore
        fan_Age_count, # type: ignore
        id_vars=['Age', 'Count'],
        var_name='Category', 
        value_name='Value'
        )
    
    # Create a bar chart using Plotly Express
    fig1 = px.bar( # type: ignore
        melted_df,
        x='Age',
        y='Value', 
        color='Category',
        barmode='group',
        hover_data={'Value': ':.0f'}, 
        labels={'Value': 'Count'},
        title='Counts by Age and Fan Categories')
    
    # Update layout and show the plot
    fig1.update_layout( # type: ignore
        xaxis_title='Age',
        yaxis_title='Count',
        legend_title='Category',
        width=1000, 
        height=500
        )
    #fig1.show() # type: ignore


    st.plotly_chart(fig1) # type: ignore
    
    st.write_stream(stream_data(insight_body))

    st.divider()
    st.divider()
    st.write_stream(stream_data("### Where are most fans from ?"))
# Count occurrences of each location
    counts = df.groupby("Location",observed=False).size().reset_index() #type: ignore
    counts.columns = ["Location", "count"]
    counts_sorted = counts.sort_values(by='count', ascending=False) #type: ignore

    fan_location_count = df.sort_values(by="Location") #type: ignore
    
    fan_location_count = df.groupby('Location',observed=False).agg( #type: ignore
        starwars_fan=('starwars_fan', 'count'),
        star_trek_fan=('star_trek_fan', 'count'),
        Expanded_universe_fan=("Expanded_universe_fan","count"),
        Count=('Location', 'size')
        ).reset_index()
    
    
    

    
    # Sort the counts DataFrame by 'count' column in ascending order
    counts_sorted = counts.sort_values(by='count', ascending=False) #type:ignore
    
    # Plotting with Plotly
    def bar_plot_plotly(df:pd.DataFrame, x:str, y:str, title:str, title_text:str) -> None: 
        fig_a = px.bar(df, x=x, y=y, title=title)#type: ignore
        fig_a.update_layout(title_text=title_text,width=1000, height=500)#type: ignore 
        #fig_a.show() #type: ignore 
        st.plotly_chart(fig_a) #type: ignore
    
        
    
    # Bar plot for fans location
    bar_plot_plotly(counts_sorted, x='Location', y='count', title='Fans Location',title_text="Fans Location") # type: ignore
    bar_plot_plotly(fan_location_count, x='Location', y='starwars_fan', title='Star Wars Fans Location',title_text="Star Wars Fans Location") # type: ignore
    bar_plot_plotly(fan_location_count, x='Location', y='star_trek_fan', title='Star Trek Fans Location',title_text="Star Trek Fans Location") # type: ignore 
    bar_plot_plotly(fan_location_count, x='Location', y='Expanded_universe_fan', title='Expanded Universe Fans Location',title_text="Expanded Universe Fans Location") # type: ignore


    st.write_stream(stream_data(fan_insight))
    

    st.divider()
    
    
    categories = ['starwars_fan', 'star_trek_fan', 'Expanded_universe_fan']
    titles = [' levels of Star Wars fans', 'levels Star Trek fans', ' levels of Expanded Universe fans']


    st.divider()
    st.write_stream(stream_data("### What are the income and Education levels of the FAN bases?"))
    categories = ['starwars_fan', 'star_trek_fan', 'Expanded_universe_fan']
    titles = ['Levels of Star Wars fans', 'Levels of Star Trek fans', 'Levels of Expanded Universe fans']
    
    # Function to create histogram plots with filtering NaN values
    def create_histogram_plot(category:str, x_column:str, title:str):
        filtered_df = df.dropna(subset=[category, x_column])  # Drop rows with NaN in the specified category and x_column #type: ignore
        if not filtered_df.empty: # type: ignore
            fig = px.histogram( #type: ignore
                filtered_df.sort_values(by="Household Income"), #type: ignore
                        x=x_column,
                        color=category, 
                        title=title,
                        histfunc='count', 
                        barmode='group'
                        )
            fig.update_layout(width=1000, height=500, margin=dict(l=20, r=20, t=70, b=20), showlegend=False) #type: ignore
            return fig
    
    # Create side-by-side histogram plots for each category
    for category, title in zip(categories, titles):
        fig1 = create_histogram_plot(category, 'Household Income', f'{title} - Household Income')
        fig2 = create_histogram_plot(category, 'Education', f'{title} - Education')
        
        if fig1 is not None: 
            #fig1.show() #type: ignore
            st.plotly_chart(fig1) #type: ignore
        
        if fig2 is not None:
            #fig2.show() #type: ignore
            st.plotly_chart(fig2) #type: ignore
        
    
    st.write_stream(stream_data("""#### INSIGHTS

Inspect the graphs  above for the income and edcation levels of the fans and non fans

"""))
    st.divider()
    st.write_stream(stream_data(" #### Thanks for viewing PART 1 of the EDA."))
    st.divider()
    
    



