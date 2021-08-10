const sqlite3 = require('sqlite3').verbose(); //Importando módulo sqlite3

/*
-----------
- SQLITE3 -
-----------
*/
let Database = new sqlite3.Database("./database/Registro.db", (err) =>{
    if (err){
        return console.error(err.message);
    }
    console.log("\n\t## Conexión a a la Base de Datos con éxito ##")
}); // Creando objeto en Database

const express = require('express'); // Importando módulo express
const http = require('http'); // Importando módulo HTTP


var app = express(); // Objeto de express (interfaz para construir servidor)


/*
---------
- HTTP -
---------
*/
// Creando servidor HTTP
var server = http.createServer(app, function(request, response){
    // Definiendo cabecera HTTP, con el estado HTTP (OK: 200) y el tipo de contenido
    response.writeHead(200, {'Content-Type': 'text/plain'});
    // Se responde, en el cuerpo de la respuesta con el mensaje "Hello World"
    response.end('Hola Mundo!\n');
}).listen(8000);
console.log("\n\t---------------------------------------------");
console.log("\n\t- Servidor en la url http://127.0.0.1:8000/ -"); // Se escribe la URL para el acceso al servidor
console.log("\n\t---------------------------------------------");

app.set('views', './views');
app.set('view engine', 'ejs');

/*
---------------
- ENRUAMIENTO -
---------------
*/

// Menu principal
app.get('/', function(request,response){
    response.render('Main');
});

// Leer datos de la Base de Datos
app.get('/Leer', function(request,response){
    const sql = "SELECT * FROM Usuarios";
    Database.all(sql, [], (err, rows) => {
        if (err){
            return console.error(err.message);
        }
        response.render('Leer.ejs',{modelo : rows});
    })
});

/*
// Crear
app.get('/Registro', function(request,response){
    response.render('Registro.ejs');
});

// Actualizar
app.get('/Actualizar', function(request,response){
    response.render('Actualizar.ejs');
});

// Eliminar
app.get('/Eliminar', function(request,response){
    response.render('Eliminar.ejs');
});
*/



// Cerrando conexión con la base de datos
app.get('/close', function(request,response){
    Database.close( (err) => {
        if (err){
            return console.error(err.message);
        }
        response.send("<center><strong>Se ha cerrado la conexión a la base de datos</strong></center>");
    })
});
