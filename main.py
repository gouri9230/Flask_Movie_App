from app import app

if __name__ == '__main__':
    app.run(debug=True)


# Things implemented/working:
# 1. User resgistration and authentication
# 2. Add a movie - take input from user
# 3. Get details of a movie
# 4. List unique movies that were added
# 5. Only accepts movie names from the available list
# 6. Add movie and view details of movie are two different endpoints.
# 7. while listing, list should be specific to current user
# 8. Delete movie
# 9. cannot take multiple entries of same movie name as input
# 10. User can rate the movie within a range