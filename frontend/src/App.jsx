import { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [plans, setPlans] = useState([]);

  const [form, setForm] = useState({
    title: "",
    discipline: "",
    summary: "",
    contents: "",
    planned_date: ""
  });

  async function loadPlans() {

    try {

      const response = await axios.get(
        "http://127.0.0.1:5000/lesson-plans"
      );

      setPlans(response.data);

    } catch (error) {

      console.log("ERRO:", error);

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
        form
      );

      alert("Plano criado com sucesso!");

      setForm({
        title: "",
        discipline: "",
        summary: "",
        contents: "",
        planned_date: ""
      });

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

    <div style={{ padding: 20 }}>

      <h1>Planos de Aula</h1>

      <form onSubmit={createPlan}>

        <input
          type="text"
          placeholder="Título"
          value={form.title}
          onChange={(e) =>
            setForm({
              ...form,
              title: e.target.value
            })
          }
        />

        <br /><br />

        <input
          type="text"
          placeholder="Disciplina"
          value={form.discipline}
          onChange={(e) =>
            setForm({
              ...form,
              discipline: e.target.value
            })
          }
        />

        <br /><br />

        <input
          type="text"
          placeholder="Resumo"
          value={form.summary}
          onChange={(e) =>
            setForm({
              ...form,
              summary: e.target.value
            })
          }
        />

        <br /><br />

        <input
          type="text"
          placeholder="Conteúdo"
          value={form.contents}
          onChange={(e) =>
            setForm({
              ...form,
              contents: e.target.value
            })
          }
        />

        <br /><br />

        <input
          type="date"
          value={form.planned_date}
          onChange={(e) =>
            setForm({
              ...form,
              planned_date: e.target.value
            })
          }
        />

        <br /><br />

        <button type="submit">
          Criar Plano
        </button>

      </form>

      <hr />

      {
        plans.length === 0
          ? (
            <p>Nenhum plano encontrado</p>
          )
          : (
            plans.map((plan) => (

              <div
                key={plan.id}
                style={{
                  border: "1px solid gray",
                  padding: 10,
                  marginBottom: 10
                }}
              >

                <h2>{plan.title}</h2>

                <p>
                  <strong>Disciplina:</strong>
                  {" "}
                  {plan.discipline}
                </p>

                <p>
                  <strong>Resumo:</strong>
                  {" "}
                  {plan.summary}
                </p>

                <p>
                  <strong>Conteúdo:</strong>
                  {" "}
                  {plan.contents}
                </p>

                <p>
                  <strong>Data:</strong>
                  {" "}
                  {plan.planned_date}
                </p>

                <button
                  onClick={() => deletePlan(plan.id)}
                >
                  Deletar
                </button>

              </div>

            ))
          )
      }

    </div>
  );
}

export default App;