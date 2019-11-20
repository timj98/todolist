# todolist
todolist Django browsable api

Using basic authentication to login.
user, user2, user3, user4 all have user_one, user_two, user_three, user_four passwords.

urls:  /todo/
GET /todo/ will get objects based on the user logged in
POST { "content": "test 67","completed": false,"created": "2019-11-20T08:55:25Z"} /todo/ will create a new user todo
PUT { "content": "test 67","completed": true,"created": "2019-11-20T06:55:25Z"} /todo/17/ will create a update where integer is the id of the object
DELETE /todo/17/ will delete if the user is the owner of the object.

In this application, used django admin to control user object permissions for brevity.
