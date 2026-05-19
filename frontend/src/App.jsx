import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [plans, setPlans] = useState([]);

  const [title, setTitle] = useState("");
  const [discipline, setDiscipline] = useState("");
  const [summary, setSummary] = useState("");
  const [contents, setContents] = useState("");
  const [plannedDate, setPlannedDate] = useState("");

  async function loadPlans() {
    try {
      const response = await axios.get(
        "http://127.0.0.1:5000/lesson-plans"
      );

      setPlans(response.data);
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    loadPlans();
  }, []);

  async function createPlan(e) {
    e.preventDefault();

    try {
      await axios.post("http://127.0.0.1:5000/lesson-plans", {
        title,
        discipline,
        summary,
        contents,
        planned_date: plannedDate,
      });

      setTitle("");
      setDiscipline("");
      setSummary("");
      setContents("");
      setPlannedDate("");

      loadPlans();
    } catch (error) {
      console.log(error);
    }
  }

  async function deletePlan(id) {
    try {
      await axios.delete(
        `http://127.0.0.1:5000/lesson-plans/${id}`
      );

      loadPlans();
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div className="container">
      <div className="header">
        <h1>Sistema de Planos de Aula</h1>
        <p>Gerencie seus planos de aula de forma simples e moderna.</p>
      </div>

      <form className="form" onSubmit={createPlan}>
        <input
          type="text"
          placeholder="Título"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Disciplina"
          value={discipline}
          onChange={(e) => setDiscipline(e.target.value)}
          required
        />

        <textarea
          placeholder="Resumo"
          value={summary}
          onChange={(e) => setSummary(e.target.value)}
        />

        <textarea
          placeholder="Conteúdo"
          value={contents}
          onChange={(e) => setContents(e.target.value)}
        />

        <input
          type="date"
          value={plannedDate}
          onChange={(e) => setPlannedDate(e.target.value)}
        />

        <button type="submit">
          Criar Plano
        </button>
      </form>

      <div className="plans-grid">
        {plans.length === 0 ? (
          <p className="empty">
            Nenhum plano encontrado
          </p>
        ) : (
          plans.map((plan) => (
            <div className="card" key={plan.id}>
              <h2>{plan.title}</h2>

              <span className="discipline">
                {plan.discipline}
              </span>

              <p>
                <strong>Resumo:</strong> {plan.summary}
              </p>

              <p>
                <strong>Conteúdo:</strong> {plan.contents}
              </p>

              <p>
                <strong>Data:</strong>{" "}
                {plan.planned_date}
              </p>

              <button
                className="delete-btn"
                onClick={() => deletePlan(plan.id)}
              >
                Deletar
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;