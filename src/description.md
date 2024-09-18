
**QUOTES API LIBRARY**

**Overview**

This Quotes API endpoint is designed to provide an easy and efficient quotes retrieval. It supports various query options, including filtering by category, author, selecting a random quote, or specifying the number of quotes to retrieve. This library is perfect for applications that need to display inspirational, humorous, thematic and other quotes to users. It comprise 500k quotes and 100+ categories and authors.
It relies on Python quotes-api library https://pypi.org/project/quotes-library/ or https://github.com/mymi14s/quotes_library

**Features**

 - **Retrieve Quotes by Category**: Users can specify a category to filter the quotes. This is useful for applications that need to display quotes relevant to specific themes or subjects.
 - **Find Quotes by Author**: This feature allows users to retrieve quotes from their favorite authors, making it easy to find wisdom from specific thinkers or writers.
 - **Random Quote Selection**: For a more spontaneous experience, users can retrieve a random quote. This feature is ideal for daily quote applications or when you want to offer users a surprise inspiration.
 - **Limit the Number of Quotes**: Users can specify how many quotes they want to retrieve, offering flexibility for different use cases, whether it's displaying a single quote of the day or a list of quotes on a particular topic.
 - **Categories**: Love, Life, Friend, Leadership, Inspiration, Emotion, Humor, Marriage, Poetry, Romance, Classis, Health, and many more.

**Usage**
Visit YOUR-IP:8000/docs in your browser to explore the API 

***Retrieve a single random quote***

    /random-quote # this is a GET method that retrieves a single quote at random 
    {'data': [{'author': 'Gayle Forman, Where She Went', 'category': 'love, romance', 'quote': "I force my eyes upward and look at Mia for the first time. She's still beautiful. Not in an obvious Vanessa LeGrande or Bryn Shraeder kind of way. In a quiet way that's always been devastating to me. Her hair, long and dark, is down now, swimming damply against her bare shoulders, which are still milky white and covered with the constellation of freckles that I used to kiss. The scar on her left shoulder, the one that used to be an angry red weld is silvery pink now. Almost like the latest rage in tattoo accessories. Almost pretty."}], 'status_code': 200, 'status_text': 'success'}

**Advanced Usage**

Here are more advanced ways to use the library:
***Retrieve Quotes by Category***:

    /get-quotes # 
    POST args include { 'category':'inspirational', 'count': 5, 'author': 'arristotle', 'random': true}

**Find Quotes by a Specific Author**:

    /get-quotes # POST args {'author': 'Mark Twain', 'count': 3}

**Get Multiple Random Quotes**:

    /get-quotes # {'random': true, 'count': 3} 

**Get Authors**:
    /get-authors {'count': 5}
    /get-authors {'count':5, 'random': true} # True|1 to randomize result
    # if no count supplied all authors will be retrieved.

**Get Categories**:
    /get-categories {'count': 5}
    get_categories {'count': 5, 'random' true} # True|1 to randomize result
    # if no count supplied, all categories will be retrieved.

**Error Handling**

The library is designed to be resilient and provide useful feedback. In case of a database connection error or query failure, it returns a structured response indicating the status code and error message.

**License**

This project is licensed under the MIT License - see the LICENSE.md file for details.

**Github**
[Quotes Library](https://github.com/mymi14s/quotes_library)
**PYPI**
[PYPI Library](https://pypi.org/project/quotes-library)
