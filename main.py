from pprintpp import pprint as pp
from db.escola import EscolaDB


def divider():
    print('\n' + '-' * 80 + '\n')


dao = EscolaDB()

while 1:    
    option = input('1. Create\n2. Read all\n3. Update teacher\n4. Delete all\n')

    if option == '1':
        pp('Digite dados do professor:')
        name = input('  Nome: ')
        age = input('  Idade: ')
        area = input('  Area: ')
        teacher = {
            'name': name,
            'age': age,
            'area': area
        }
        pp('Digite dados da materia:')
        matter = input(' Assunto: ')
        time = input(' Horario: ')
        matterTime = input(' O professor leciona a materia desde que ano: ')
        classroom = {
            'matter': matter,
            'time': time,
            'matterTime': matterTime
        }
        aux = dao.create(teacher, classroom)
        divider()

    elif option == '2':
        aux = dao.read_all_nodes()
        pp(aux)
        divider()

    elif option == '3':
        nameEdit = input('Digite o nome de quem deseja editar:')
        pp('Digite dados do professor:')
        name = input('  Nome: ')
        age = input('  Idade: ')
        area = input('  Area: ')
        teacher = {
            'name': name,
            'age': age,
            'area': area
        }
        aux = dao.update(nameEdit, teacher)
        divider()

    elif option == '4':
        aux = dao.delete_all_nodes()
        divider()

    else:
        break

dao.db.close()
