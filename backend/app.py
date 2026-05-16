from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

app = Flask(__name__)

# Configuração do banco SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# Model da tabela
class LessonPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    objective = db.Column(db.Text)
    summary = db.Column(db.Text)
    planned_date = db.Column(db.String(100))
    discipline = db.Column(db.String(100))
    contents = db.Column(db.Text)
    support_resources = db.Column(db.Text)
    tags = db.Column(db.Text)


# Cria o banco automaticamente
with app.app_context():
    db.create_all()


# Rota inicial
@app.route('/')
def home():
    return {"message": "API funcionando"}


# Health check
@app.route('/health')
def health():
    return {"status": "ok"}


# Criar plano de aula
@app.route('/lesson-plans', methods=['POST'])
def create_plan():
    data = request.json

    plan = LessonPlan(
        title=data['title'],
        objective=data.get('objective'),
        summary=data.get('summary'),
        planned_date=data.get('planned_date'),
        discipline=data.get('discipline'),
        contents=data.get('contents'),
        support_resources=data.get('support_resources'),
        tags=data.get('tags')
    )

    db.session.add(plan)
    db.session.commit()

    return jsonify({
        "message": "Plano criado com sucesso"
    }), 201


# Listar todos os planos
@app.route('/lesson-plans', methods=['GET'])
def get_plans():
    plans = LessonPlan.query.all()

    result = []

    for plan in plans:
        result.append({
            "id": plan.id,
            "title": plan.title,
            "objective": plan.objective,
            "summary": plan.summary,
            "planned_date": plan.planned_date,
            "discipline": plan.discipline,
            "contents": plan.contents,
            "support_resources": plan.support_resources,
            "tags": plan.tags
        })

    return jsonify(result)


# Buscar plano por ID
@app.route('/lesson-plans/<int:id>', methods=['GET'])
def get_plan(id):
    plan = LessonPlan.query.get_or_404(id)

    return jsonify({
        "id": plan.id,
        "title": plan.title,
        "objective": plan.objective,
        "summary": plan.summary,
        "planned_date": plan.planned_date,
        "discipline": plan.discipline,
        "contents": plan.contents,
        "support_resources": plan.support_resources,
        "tags": plan.tags
    })


# Atualizar plano
@app.route('/lesson-plans/<int:id>', methods=['PUT'])
def update_plan(id):
    plan = LessonPlan.query.get_or_404(id)

    data = request.json

    plan.title = data['title']
    plan.objective = data.get('objective')
    plan.summary = data.get('summary')
    plan.planned_date = data.get('planned_date')
    plan.discipline = data.get('discipline')
    plan.contents = data.get('contents')
    plan.support_resources = data.get('support_resources')
    plan.tags = data.get('tags')

    db.session.commit()

    return jsonify({
        "message": "Plano atualizado com sucesso"
    })


# Remover plano
@app.route('/lesson-plans/<int:id>', methods=['DELETE'])
def delete_plan(id):
    plan = LessonPlan.query.get_or_404(id)

    db.session.delete(plan)
    db.session.commit()

    return jsonify({
        "message": "Plano removido com sucesso"
    })

@app.route("/recommendations", methods=["POST"])
def generate_recommendations():
    data = request.json

    prompt = f"""
    Gere uma recomendação de plano de aula sobre:
    Disciplina: {data.get("discipline")}
    Tema: {data.get("topic")}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content

        return jsonify({
            "success": True,
            "recommendation": content
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "API da OpenAI sem créditos ou indisponível.",
            "error": str(e)
        }), 500

# Inicialização do servidor
if __name__ == '__main__':
    app.run(debug=True)