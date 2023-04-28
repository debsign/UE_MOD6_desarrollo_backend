// https://github.com/fanzeyi/pokemon.json/blob/master/pokedex.json

const http = require('http');
const https = require('https');

const fetchPokemonData = async () => {
  return new Promise((resolve, reject) => {
    https.get('https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json', (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        resolve(JSON.parse(data));
      });

    }).on('error', (err) => {
      reject(err);
    });
  });
};

const handleRequest = async (req, res) => {
  const pokemonNameId = decodeURI(req.url.substring(1));

  if(!pokemonNameId) {
    res.writeHead(400, {'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Añade un ID o nombre de Pokemon válido. Ejemplo: localhost:3000/Pikachu');
  }

  const pokedexData = await fetchPokemonData();

  const pokemonData = pokedexData.find(pokemon => 
    (Object.values(pokemon.name).some(name => name === pokemonNameId) || pokemon.id === parseInt(pokemonNameId))
  );

  if (pokemonData) {
    const response = {
      'Tipo': pokemonData.type,
      'HP': pokemonData.base["HP"],
      'Attack': pokemonData.base["Attack"],
      'Defense': pokemonData.base["Defense"],
      'Sp. Attack': pokemonData.base["Sp. Attack"],
      'Sp. Defense': pokemonData.base["Sp. Defense"],
      'Speed': pokemonData.base["Speed"],
    };
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(response, null, 2));
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Pokemon no encontrado');
  }
};

const server = http.createServer(handleRequest);

server.listen(3000, () => {
  console.log('Servidor escuchando en el puerto 3000');
});
