
const express = require('express');
const mongoose = require('mongoose');
const app = express();

require('./database');
// middleware para analizar el cuerpo de la solicitud HTTP con formato JSON 
// y convertirlo en un objeto JavaScript para usarlo en el objeto req.body.
app.use(express.json());

const PORT = 3000;
const CLIENT_ID = 'd3426323535d4990beed49b3792a325f';
const CLIENT_SECRET = 'b626ea3f993448729242bbe9bd2019a2';
const SPOTIFY_API_TOKEN = 'BQBIwMuBwpU3WxZoEf3SAbMrlVPB9hXXEX06UlzctiIBvVYFL7VWpIhPSYX1cXy0Yaw5bjmGFeIChydkJWygcPFHB1O0plHsry2pNDSejS3B3X2-HfFY6zyVVpJsFa4qSN5S2mpulpNuxuafDu8bOBYFLOTaCV4q9GwyMl-ZcU9TV6Czb027';

// Obtener canciones más escuchadas en Spotify
const apiFavSongs = 'https://api.spotify.com/v1/me/top/tracks';

app.get('/songs', async(req, res) => {
    try {
        const response = await fetch(apiFavSongs, {
            headers: {
                'Authorization': `Bearer ${SPOTIFY_API_TOKEN}`
            }
        });
        // Convertir la respuesta de la API en formato JSON en un objeto
        // await para esperar a que se complete la promesa devuelta por response.json()
        const data = await response.json();
        const songNames = data.items.map(item => ({ 
            id: item.album.id,
            titulo: item.album.name, 
            external_urls: item.album.external_urls.spotify, 
            artists: item.artists.map(artist => artist.name)
        }))
        res.send({ items: songNames });
    } catch(error) {
        console.error('Error al obtener las canciones');
        res.status(500).send({error: error.message});
    }
})

// Definimos el esquema
const favSongsSchema = new mongoose.Schema({
    titulo: { type:String, required: true },
    external_urls: String,
    artists: String,
});

// Le asignamos el modelo a la canción
const Cancion = mongoose.model('Cancion', favSongsSchema);


// CRUD
// Ejemplo:
// {
//     "titulo": "As it was",
//     "external_urls": "https://open.spotify.com/track/4Dvkj6JhhA12EX05fT7y2e?si=93185b3c0e9e49bd",
//     "artists": "Harry Styles"
// }
// GET
app.get('/fav-songs', async (req, res) => {
    try {
      const canciones = await Cancion.find();
      res.send(canciones);
    } catch (error) {
      console.error('Error al obtener las canciones', error);
      res.status(500).send({ error: error.message });
    }
  });

// POST
app.post('/fav-songs', async (req, res) => {
    try {
        // Agrega la desestructuración de la solicitud para obtener el título
        const { titulo, external_urls, artists } = req.body; 
        // Verificar si la canción ya existe en la base de datos
        const existingSong = await Cancion.findOne({ titulo });
        if (existingSong) {
            console.error('La canción ya existe en esta lista');
            res.status(409).send({ error: 'La canción ya existe en esta lista' });
        }
        
      const cancion = new Cancion({ titulo, external_urls, artists });
      await cancion.save();
      res.status(201).send(cancion);
    } catch (error) {
      console.error('Error al crear la canción', error);
      res.status(500).send({ error: error.message });
    }
  });

// PUT
app.put('/fav-songs/:id', async(req, res) => {
    try {
        const cancion = await Cancion.findByIdAndUpdate(req.params.id, req.body);
        if (!cancion) {
            return res.status(404).send({error: 'Canción no encontrada'});
        } 
        res.send(cancion);
    } catch {
        res.status(500).send({error: error.message});
    }
});

// DELETE
app.delete('/fav-songs/:id', async (req, res) => {
    try {
        const cancion = await Cancion.findByIdAndDelete(req.params.id);
        // Así personalizamos mejor el error que nos pueda dar
        if (!cancion) {
            return res.status(404).send({error: 'Cancion no encontrada'});
        }
        res.send(cancion);
    } catch(error) {
        res.status(500).send({error: error.message});
    }
});

app.listen(PORT, () => {
    console.log(`Servidor escuchando en el puerto ${PORT}`)
});
