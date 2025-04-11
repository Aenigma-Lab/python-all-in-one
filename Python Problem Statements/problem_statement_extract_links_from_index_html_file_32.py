# extract links from index.html file 

# very easy  solution but not the best  😒😒😒😒

# the problem in this solution is it will extract only 1 line in a line
# if have multiple link in line then it will fail to extract 2nd links in same line.

# with open('index.html','r') as webpage:
#     with open('urls.txt', 'a') as tf:
#         for line in webpage.readlines():
#             if "<a href=" in line:
#                 url_line = line.find("<a href=")
#                 url_start_quote = line.find('\"',url_line)
#                 url_end_quote = line.find('\"',url_start_quote+1)

#                 urls = line[url_start_quote+1:url_end_quote]
#                 tf.write(urls+ "\n")

   

# best solution✅✅✅✅✅😊😊😊😊 


# Open the input HTML file in read mode and the output text file in append mode
with open('index.html', 'r') as webpage:
    with open('urls.txt', 'a') as tf:
        # Read the content of the HTML page
        page = webpage.read()
        
        # Initialize a flag to check for the existence of links
        link_exist = True
        
        # Loop until no more links are found
        while link_exist:
            # Find the start of the <a href="..."> tag
            point_of_start = page.find("<a href=")
            
            # If no <a href= is found, stop the loop
            if point_of_start == -1:
                link_exist = False
            else:
                # Find the starting and ending quotes of the URL
                url_start_quote = page.find('"', point_of_start)
                url_end_quote = page.find('"', url_start_quote + 1)
                
                # Extract the URL between the quotes
                url = page[url_start_quote + 1:url_end_quote]
                
                # Write the URL to the output file
                tf.write(url + "\n")
                
                # Update the page content to process remaining links
                page = page[url_end_quote:]


