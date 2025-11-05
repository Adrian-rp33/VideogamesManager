<h1>Console Videogame Manager</h1>
<p>
  Console Videogame management app, it uses basic CRUD operations such as list, add, modify and delete
  to fully control all the videogames data. This version only allows to have all the data loaded on execution, 
  it won't persist it anywhere.
</p>
<br/>
<h2>How to use</h2>
<p>
  On launch, you'll see the menu with 5 different options:
  <br/>
  List -> Show all the videogames that are currently in, if there is no games, it'll warm the user.
  <br/>
  Add -> Allows the user to create a videogame to add into the games list.
  <br/>
  Modify -> Using one game's id , it'll will allow to change any info about that game (except for the id).
  <br/>
  Delete -> Using one game's id, it'll allow the user to delete one game from the list.
  <br/>
  Exit -> Closes the program.
</p>
<h2>Architecture</h2>
<p>
  This program uses a MVC architecture, which is divided like this:
  <ul>
    <li>
      <p>
        <strong>Model: </strong>Videogame DTO, which contains id, name, price, tags, release year. Each 
        one of them having a type asinged, for example id -> int, name -> string, price -> float, ...
      </p>
    </li>
    <li>
      <p>
        <strong>View: </strong>It consist on the main file which starts and ends the execution, the user will
        use this as a way to interact with the app.
      </p>
    </li>
    <li>
      <p>
        <strong>Controller: </strong>Most of the App is located here, it manages and has the list where all the videogames
        are added, and since it check all of the data that the user enters, it handle most of the possible errors that can happen.
        <br/>
        As mentioned before, id cannot be changed, becouse this class creates it using the highest previus id, for example if there are 3 games 
        the higher id is 3, so adding another game will have the id 4, even if the games with id 2 or 1 are deleted.
      </p
    </li>
  </ul>
</p>
<h2></h2>
