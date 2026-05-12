import { useState, useEffect } from 'react'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [tasks, setTasks] = useState([])
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  // Aufgaben beim ersten Laden abrufen
  const fetchTasks = async () => {
    setLoading(true)
    try {
      const res = await fetch(`${API_URL}/tasks`)
      if (!res.ok) throw new Error('Fehler beim Laden der Aufgaben')
      const data = await res.json()
      setTasks(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchTasks()
  }, [])

  // Neue Aufgabe erstellen
  const addTask = async (e) => {
    e.preventDefault()
    if (!title.trim()) return

    try {
      const res = await fetch(`${API_URL}/tasks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description, completed: false })
      })
      if (!res.ok) throw new Error('Fehler beim Erstellen')
      await fetchTasks()
      setTitle('')
      setDescription('')
    } catch (err) {
      setError(err.message)
    }
  }

  // Aufgabe als erledigt / nicht erledigt markieren
  const toggleComplete = async (task) => {
    try {
      const res = await fetch(`${API_URL}/tasks/${task.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed: !task.completed })
      })
      if (!res.ok) throw new Error('Fehler beim Aktualisieren')
      await fetchTasks()
    } catch (err) {
      setError(err.message)
    }
  }

  // Aufgabe löschen
  const deleteTask = async (id) => {
    try {
      const res = await fetch(`${API_URL}/tasks/${id}`, {
        method: 'DELETE'
      })
      if (!res.ok) throw new Error('Fehler beim Löschen')
      await fetchTasks()
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div className="container">
      <header className="header">
        <h1>🗑️ Aufgabenlöscher</h1>
        <p>Verwalte deine Aufgaben professionell</p>
      </header>

      {error && (
        <div className="error-banner">
          {error}
          <button onClick={() => setError(null)}>×</button>
        </div>
      )}

      <form className="task-form" onSubmit={addTask}>
        <input
          type="text"
          placeholder="Neue Aufgabe..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Beschreibung (optional)"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <button type="submit">Hinzufügen</button>
      </form>

      <section className="task-list">
        <h2>Deine Aufgaben ({tasks.length})</h2>
        {loading ? (
          <p className="info">Lade Aufgaben...</p>
        ) : tasks.length === 0 ? (
          <p className="info">Keine Aufgaben vorhanden. Erstelle eine neue!</p>
        ) : (
          <ul>
            {tasks.map((task) => (
              <li key={task.id} className={task.completed ? 'completed' : ''}>
                <div className="task-content">
                  <strong>{task.title}</strong>
                  {task.description && <span>{task.description}</span>}
                </div>
                <div className="task-actions">
                  <button
                    className="toggle-btn"
                    onClick={() => toggleComplete(task)}
                    title={task.completed ? 'Rückgängig' : 'Erledigt'}
                  >
                    {task.completed ? '↩️' : '✅'}
                  </button>
                  <button
                    className="delete-btn"
                    onClick={() => deleteTask(task.id)}
                    title="Löschen"
                  >
                    🗑️
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </section>

      <footer className="footer">
        <p>Aufgabenlöscher v1.0 — IT-Administrator Projekt</p>
      </footer>
    </div>
  )
}

export default App
