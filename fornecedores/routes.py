from flask import render_template, request, redirect, url_for, flash
from fornecedores import fornecedores_bp # Importa a instância do blueprint
from .models import Fornecedores 
from app import db

# Lista todos os fornecedores
@fornecedores_bp.route('/')
def index():
    suppliers = Fornecedores.query.all() # Busca todos os fornecedores no banco de dados
    return render_template('fornecedores/index.html', suppliers=suppliers)

# criar um novo fornecedor 
@fornecedores_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        contact_person = request.form['contact_person']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        # Validação 
        if not name or not phone:
            flash('Nome e Telefone são campos obrigatórios!', 'danger')
            return redirect(url_for('suppliers.create'))

        new_fornecedor = Fornecedores(
            name=name,
            contact_person=contact_person,
            phone=phone,
            email=email,
            address=address
        )
        try:
            db.session.add(new_fornecedor) # 
            db.session.commit() # 
            flash('Fornecedor adicionado com sucesso!', 'success')
            return redirect(url_for('fornecedores.index'))
        except Exception as e:
            db.session.rollback() 
            flash(f'Erro ao adicionar fornecedores: {e}', 'danger')
            return redirect(url_for('fornecedores.create'))

    return render_template('fornecedores/create.html') 

# editar um fornecedor 
@fornecedores_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    fornecedores = Fornecedores.query.get_or_404(id) 

    if request.method == 'POST':
        fornecedores.name = request.form['name']
        fornecedores.contact_person = request.form['contact_person']
        fornecedores.phone = request.form['phone']
        fornecedores.email = request.form['email']
        fornecedores.address = request.form['address']

        # Validação b
        if not fornecedores.name or not fornecedores.phone:
            flash('Nome e Telefone são campos obrigatórios!', 'danger')
            return redirect(url_for('fornecedores.edit', id=fornecedores.id))

        try:
            db.session.commit() 
            flash('Fornecedor atualizado com sucesso!', 'success')
            return redirect(url_for('fornecedores.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar fornecedor: {e}', 'danger')
            return redirect(url_for('fornecedores.edit', id=fornecedores.id))

    return render_template('fornecedores/edit.html', fornecedores=fornecedores)

# deletar um fornecedor 
@fornecedores_bp.route('/delete/<int:id>', methods=['POST']) 
def delete(id):
    fornecedores = Fornecedores.query.get_or_404(id)

    try:
        db.session.delete(fornecedores) 
        db.session.commit() 
        flash('Fornecedor deletado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao deletar fornecedor: {e}', 'danger')

    return redirect(url_for('fornecedores.index'))