import { useEffect, useState } from "react";
import axios from "axios";
import {
  FaBook,
  FaTrash,
  FaPlus,
  FaSearch,
} from "react-icons/fa";

import "./App.css";

function App() {
  const [plans, setPlans] = useState([]);

  const [title, setTitle] = useState("");
  const [discipline, setDiscipline] = useState("");
  const [summary, setSummary] = useState("");
  const [contents, setContents] = useState("");
  const [plannedDate, setPlannedDate] =
    useState("");

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
      await axios.post(
        "http://127.0.0.1:5000/lesson-plans",
        {
          title,
          discipline,
          summary,
          contents,
          planned_date: plannedDate,
        }
      );

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
    <div className="app">
      <aside className="sidebar">
        <h1>
          <FaBook />
          Lesson Planner
        </h1>

        <p>
          Sistema moderno de gerenciamento
          de planos de aula.
        </p>

        <div className="stats">
          <span>Total de planos</span>
          <strong>{plans.length}</strong>
        </div>
      </aside>

      <main className="content">
        <div className="topbar">
          <div className="search-box">
            <FaSearch />

            <input
              type="text"
              placeholder="Buscar planos..."
            />
          </div>
        </div>

        <section className="form-container">
          <h2>Criar Plano</h2>

          <form onSubmit={createPlan}>
            <input
              type="text"
              placeholder="Título"
              value={title}
              onChange={(e) =>
                setTitle(e.target.value)
              }
            />

            <input
              type="text"
              placeholder="Disciplina"
              value={discipline}
              onChange={(e) =>
                setDiscipline(e.target.value)
              }
            />

            <textarea
              placeholder="Resumo"
              value={summary}
              onChange={(e) =>
                setSummary(e.target.value)
              }
            />

            <textarea
              placeholder="Conteúdo"
              value={contents}
              onChange={(e) =>
                setContents(e.target.value)
              }
            />

            <input
              type="date"
              value={plannedDate}
              onChange={(e) =>
                setPlannedDate(e.target.value)
              }
            />

            <button type="submit">
              <FaPlus />
              Criar Plano
            </button>
          </form>
        </section>

        <section className="cards">
          {plans.length === 0 ? (
            <p>Nenhum plano encontrado.</p>
          ) : (
            plans.map((plan) => (
              <div className="card" key={plan.id}>
                <div className="card-header">
                  <h3>{plan.title}</h3>

                  <span>
                    {plan.discipline}
                  </span>
                </div>

                <p>
                  <strong>Resumo:</strong>{" "}
                  {plan.summary}
                </p>

                <p>
                  <strong>Conteúdo:</strong>{" "}
                  {plan.contents}
                </p>

                <p>
                  <strong>Data:</strong>{" "}
                  {plan.planned_date}
                </p>

                <button
                  onClick={() =>
                    deletePlan(plan.id)
                  }
                >
                  <FaTrash />
                  Deletar
                </button>
              </div>
            ))
          )}
        </section>
      </main>
    </div>
  );
}

export default App;