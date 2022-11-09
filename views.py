from flask import render_template, request, redirect
from app import app
from database import db
from models import Employee


@app.route('/', methods=['GET'])
def main():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route('/', methods=['POST'])
def insert():
    employee_get = request.form.to_dict()

    employee = Employee(
        name=employee_get.get('name', ''),
        email=employee_get.get('email', ''),
        phone=employee_get.get('phone', '')
    )
    db.session.add(employee)
    db.session.commit()
    return redirect('/')


@app.route('/update', methods=['POST'])
def update():
    employee_data = request.form.to_dict()
    employee = Employee.query.get(employee_data.get('id'))
    employee.name = employee_data.get('name')
    employee.email = employee_data.get('email')
    employee.phone = employee_data.get('phone')
    db.session.add(employee)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:eid>', methods=['GET'])
def delete(eid):
    result = db.session.query(Employee).filter(Employee.id == eid).one()
    db.session.delete(result)
    db.session.commit()
    return redirect('/')
