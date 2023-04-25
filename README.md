<h1 align="center">
    <br>
    <a href="https://www.aresworkout.tk">
        <img src="https://user-images.githubusercontent.com/97703272/199109650-0f7a2bf0-a102-463d-bc19-af712ab43cc8.png" alt="Ares Workout" width="200">
    </a>
    <br>
    Ares Workout
    <br>
</h1>

<h4 align="center">A minimal workout tracker web app built with <a href="https://flask.palletsprojects.com/" target="_blank">Flask.</a></h4>

<p align="center">
    <a href="#about">About</a> •
    <a href="#video-demo">Video Demo</a> •
    <a href="#how-to-use">How to Use</a> •
    <a href="#license">License</a> •
    <a href="#acknowledgments">Acknowlegments</a> •
    <a href="#contact">Contact</a>
</p>

![Screenshots](https://user-images.githubusercontent.com/97703272/175546196-259a3f7c-5ea3-47ba-bd68-d895663ef473.png)

## About

While there are many excellent workout trackers available, I always found myself going back to my good old notes after trying them out for a while. I felt overwhelmed by their complexity and craved a simple way to track my weights and machine adjustments at a glance. That's why I created Ares!

Ares is a minimalist workout tracker built with Flask, Python, SQLAlchemy, JavaScript, and pure CSS. It allows users to create workouts with multiple exercises and store weights and details for each one. With Ares, you can quickly switch between workouts and easily make edits. It was designed to be a practical solution for those who want to track their progress while maintaining efficiency.

### Built With

-   [Flask](https://flask.palletsprojects.com/)
-   [Python](https://www.python.org/)
-   [JavaScript](https://www.javascript.com/)
-   [SQLAlchemy](https://www.sqlalchemy.org/)
-   [PostgreSQL](https://www.postgresql.org/)
-   [Figma](https://www.figma.com/ui-design-tool/)

## Video Demo

https://user-images.githubusercontent.com/97703272/176287446-cadcaab4-0c77-41ae-b85c-5afe05d0465a.mp4

## How to Use

| Screenshot | Instructions |
|--|--|
| ![Sign in](https://user-images.githubusercontent.com/97703272/234174007-5f0b9160-a88c-4c39-9b4a-a9a3a15e6747.png) | To access the app, you have two options: create a new account or sign in with a demo user. If you choose to sign in with a demo user, a brand new account will be generated for one-time use. |
| ![Home](https://user-images.githubusercontent.com/97703272/234174024-ab6e31c4-c243-4055-b4a1-5b0322b788b6.png) | Once you're signed in, click on "Add workout" to create your first workout. |
| ![Add workout](https://user-images.githubusercontent.com/97703272/234174042-5ebde671-2083-43fe-b74e-6515f7db2db1.png) | Give your workout a name with 1-12 characters and optionally, a short description with up to 18 characters. |
| ![Add exercises](https://user-images.githubusercontent.com/97703272/234174050-72d65cf8-94fc-47e5-9ee8-748c10380c89.png) | Start adding exercises by giving them names (up to 45 characters) and selecting whether to include details like machine adjustments, number of reps, etc. To add more exercises, simply click the "+" button under the existing ones. |
| ![Reorder exercises](https://user-images.githubusercontent.com/97703272/234174394-39d1e76b-05ec-4424-8f28-adef6149a376.png) | You can both delete and reorder exercises. To delete an exercise, click the "X" button on the desired one. To reorder exercises, click and drag the "=" button and move the exercise to the new location. |
| ![Created workout](https://user-images.githubusercontent.com/97703272/234174412-97719137-6187-4bb3-a6f9-bb7e6145cf6b.png) | Once you're satisfied with the workout, click "Save workout". You'll be redirected to the home page where you'll see your newly created workout. |
| ![Edit workout](https://user-images.githubusercontent.com/97703272/234174503-c51ae570-66c0-428e-a9de-824a3a5c6e66.png) | If you wish to make any changes, click the pencil icon to edit the workout. This will take you to a page where you can modify any previous steps. You can also delete the workout by clicking the grey "Delete workout" button at the bottom of the page. |
| ![Delete workout](https://user-images.githubusercontent.com/97703272/234174511-5f32a31b-3eb3-4631-980f-0a1fa3459abb.png) | You'll be prompted to confirm your choice since all exercises will be deleted, and the process is irreversible. To confirm the deletion, press "Delete". |
| ![Workout page](https://user-images.githubusercontent.com/97703272/234174420-52b94514-e839-4977-85e2-15d6af35bf39.png) | To access any workout from the home page, simply click on the desired one. You'll be taken to the workout page where all exercises are listed, but no weights or details have been added yet. Notice that you can quickly switch between workouts using the top dropdown menu. |
| ![Edit info](https://user-images.githubusercontent.com/97703272/234174444-e04d6cc7-31dc-42aa-8545-55c6e437b8ac.png) | To add weights and details, click the orange "Edit" button at the bottom of the page. This will unlock the inputs on each exercise where you can enter all the necessary information. |
| ![Updated info](https://user-images.githubusercontent.com/97703272/234174458-9b7e7138-5787-4db7-9956-b490670b5218.png) | Once you've input everything, click "Save changes", and the page will be updated. |

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgments

-   [SortableJS](https://github.com/SortableJS/Sortable)
-   [Werkzeug](https://werkzeug.palletsprojects.com)

## Contact

Bruno Samuel - [LinkedIn](https://www.linkedin.com/in/brunosag/) - brunosag@outlook.com.br
