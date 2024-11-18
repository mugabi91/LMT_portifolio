
################### page Home ######################################
page_one_name = "Home"

page_one_title = "# lmt data analysis portifolio" 

bio = """ ###### By. L Mugabi Trevor. 
        Welcome to my portifolio.
        """


intro = """ #### Introduction to the Star Wars Franchise Dataset:

The Star Wars franchise is one of the most iconic and beloved series in the history of popular culture. It encompasses a vast universe filled with memorable characters, epic battles, and intricate lore. For those unfamiliar with the franchise, Star Wars began as a groundbreaking film created by George Lucas in 1977, titled "Star Wars: Episode IV - A New Hope". Since then, it has expanded into a multimedia phenomenon, including movies, TV shows, books, comics, video games, and more.

The Star Wars franchise dataset provides a comprehensive collection of data related to various aspects of this expansive universe. It includes information about characters, planets, starships, vehicles, species, and much more. This dataset offers valuable insights into the rich tapestry of the Star Wars universe, allowing fans and researchers alike to explore and analyze different elements of the franchise.

Whether you're interested in learning about the iconic."""


dataset_subtitle = "#### Original dataset:"

startrek_subtitle = "#### The dataset also holds data on star trek:"

startrek_bio = """ The Star Trek franchise is a beloved and iconic science fiction universe that has captivated audiences worldwide for decades. It originated as a television series created by Gene Roddenberry in the 1960s and has since expanded into a vast multimedia phenomenon including TV shows, movies, books, games, and more.

    At its core, Star Trek is known for its optimistic vision of the future, exploring themes of exploration, diversity, cooperation, and the quest for knowledge. Set in the distant future, it follows the adventures of Starfleet, a space-exploration organization representing the United Federation of Planets. The franchise features a diverse cast of characters from different species and backgrounds, working together aboard starships like the iconic USS Enterprise to discover new worlds, encounter alien civilizations, and tackle moral and ethical dilemmas.

    Star Trek is renowned for its groundbreaking representation, including one of the first multicultural casts on television and addressing social issues through allegorical storytelling. It has inspired generations of fans (known as Trekkies or Trekkers) and has become a cultural touchstone for its exploration of humanity's potential, the wonders of space exploration, and the importance of cooperation and understanding in a vast and diverse universe."""
    


################### page EDA ######################################
page_two_name = "EDA"
page_2_title = "# Exploratory Data Analysis (EDA)"




drop_columns =[  # type: ignore
            'Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7',
            'Unnamed: 8','Unnamed: 10','Unnamed: 11','Unnamed: 12',
            'Unnamed: 13','Unnamed: 14','Unnamed: 16','Unnamed: 17',
            'Unnamed: 18','Unnamed: 20','Unnamed: 19','Unnamed: 20',
            'Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24',
            'Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28'
            ] 


rename_columns_dict = {
    'Have you seen any of the 6 films in the Star Wars franchise?':"watched_starwars",
    'Do you consider yourself to be a fan of the Star Wars film franchise?':"starwars_fan",
    'Which of the following Star Wars films have you seen? Please select all that apply.':'watched_starwars_films',
    'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.':'ranking',
    'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.':"taste_character",
    'Which character shot first?':'fired_first',
    'Are you familiar with the Expanded Universe?':'knowledge_of_expanded_universe',
    'Do you consider yourself to be a fan of the Expanded Universe?æ':'Expanded_universe_fan',
    'Do you consider yourself to be a fan of the Star Trek franchise?':'star_trek_fan',
    'Location (Census Region)':"Location"

    }

null_number_title = "#### The total number of nulls in each variable in the DataSet are below:"
observation_title ='### Observation'
insight_body = ''' #### INSIGHTS
    As seen above star trek has got the highest number of fans followed by star wars and last the expanded universe

    The fan make up by gender shows its mostly Males interested in the franchises except for startrek where the female fan base is greater than the male fan base

    For starwars it has mostly a fan base of people aged 30 to 60 yrs of age

    For star_trek, it has mostly a fan base of people 45 to 60 yrs of age

    For the expanded universe, it has a fan base mainly of younger people of ages 18 to 44 yrs

    Looking at the female fan base of all the franchises, starwars has the highest female base compared to the others. star trek comes in second and the expanded universe comes in last

    Looking at the male fan base of all the franchises, starwars has the highest male fan base compared to the others. star trek comes in second and the expanded universe comes in last'''
    
fan_insight = """#### INSIGHTS
    Most fans are from the East North Central followed by the pacific and then the south Atlantic

    Inspect the graphs  above for the rest and more insight on location of fans and non fans locations

    """
