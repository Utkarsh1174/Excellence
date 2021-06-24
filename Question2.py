import requests


# Function generates url by using the page number which is passed as i
def url_generator(i) -> object:
    link = (f"https://reqres.in/api/users?page={i}")
    return link


# Function finds total number of users by going through all the pages
def total_number_of_users():
    total_users = 0
    for i in range(1, 13):  # using for loop to generate page numbers
        link = url_generator(i)     # calling the url_generator function and passing the page number
        response = requests.get(url=link)
        response.raise_for_status()
        data = response.json()
        total_users += data['per_page']
    print(f"Total number of users={total_users}")


total_number_of_users()
