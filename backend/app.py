from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


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

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "objective": self.objective,
            "summary": self.summary,
            "planned_date": self.planned_date,
            "discipline": self.discipline,
            "contents": self.contents,
            "support_resources": self.support_resources,
            "tags": self.tags
        }


# Cria o banco automaticamente
with app.app_context():
    db.create_all()


# Rota inicial
@app.route('/')
def home():
    return {
        "message": "API funcionando"
    }


# Health check
@app.route('/health')
def health():
    return {
        "status": "ok"
    }


# Criar plano de aula
@app.route('/lesson-plans', methods=['POST'])
def create_plan():

    data = request.json

    if not data.get("title"):
        return jsonify({
            "error": "Título é obrigatório"
        }), 400

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
        "message": "Plano criado com sucesso",
        "data": plan.to_dict()
    }), 201


# Listar todos os planos
@app.route('/lesson-plans', methods=['GET'])
def get_plans():

    plans = LessonPlan.query.all()

    return jsonify([
        plan.to_dict() for plan in plans
    ])


# Buscar plano por ID
@app.route('/lesson-plans/<int:id>', methods=['GET'])
def get_plan(id):

    plan = LessonPlan.query.get_or_404(id)

    return jsonify(plan.to_dict())


# Buscar por disciplina
@app.route('/lesson-plans/discipline/<string:discipline>', methods=['GET'])
def get_by_discipline(discipline):

    plans = LessonPlan.query.filter_by(
        discipline=discipline
    ).all()

    return jsonify([
        plan.to_dict() for plan in plans
    ])


# Paginação
@app.route('/lesson-plans/paginated', methods=['GET'])
def paginated_plans():

    page = request.args.get('page', 1, type=int)
    per_page = 2

    plans = LessonPlan.query.paginate(
        page=page,
        per_page=per_page
    )

    return jsonify({
        "page": page,
        "total": plans.total,
        "pages": plans.pages,
        "data": [plan.to_dict() for plan in plans.items]
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
        "message": "Plano atualizado com sucesso",
        "data": plan.to_dict()
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


# Recomendações sem OpenAI
@app.route('/recommendations', methods=['POST'])
def generate_recommendations():

    data = request.json

    discipline = data.get("discipline")
    topic = data.get("topic")

    recommendation = {
        "title": f"Aula sobre {topic}",
        "objective": f"Ensinar os conceitos principais de {topic}",
        "summary": f"Aula introdutória da disciplina de {discipline} sobre {topic}.",
        "contents": f"Conceitos fundamentais de {topic}",
        "support_resources": "Slides, vídeos e exercícios",
        "tags": f"{discipline.lower()},{topic.lower()}"
    }

    return jsonify({
        "success": True,
        "recommendation": recommendation
    })


# Inicialização do servidor
if __name__ == '__main__':
    app.run(debug=True)