const express = require('express');
const app = express();
app.use(express.json());

let tasks = [];

app.get('/tasks', (req, res) => {
    res.json(tasks);
});

app.post('/tasks', (req, res) => {
    const task = req.body;
    tasks.push(task);
    res.status(201).json(task);
});

app.put('/tasks/:id', (req, res) => {
    const id = req.params.id;
    const updatedTask = req.body;
    tasks = tasks.map(task => task.id == id ? updatedTask : task);
    res.json(updatedTask);
});

app.delete('/tasks/:id', (req, res) => {
    const id = req.params.id;
    tasks = tasks.filter(task => task.id != id);
    res.status(204).end();
});

app.listen(3000);
