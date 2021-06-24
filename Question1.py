import requests


# gets the data from the posts api and return the response
def get_posts_api():
    response = requests.get(url="https://my-json-server.typicode.com/typicode/demo/posts")
    response.raise_for_status()
    return response


# gets the data from the comments api and return the response
def get_comments_api():
    response = requests.get(url="https://my-json-server.typicode.com/typicode/demo/comments")
    response.raise_for_status()
    return response


data_post = get_posts_api().json()
data_comments = get_comments_api().json()
for post_items in data_post:
    comment_list = []
    for comment_items in data_comments:

        comment_dict = {}
        comment_dict.clear()
        if post_items['id'] == comment_items['postId']:
            # post_items['comments']=comment_items['body']
            comment_dict['id'] = comment_items['id']
            comment_dict['body'] = comment_items['body']
            comment_list.append(comment_dict)
        post_items['comments'] = comment_list

print(data_post)
