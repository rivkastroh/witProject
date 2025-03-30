from Repository import Repository
import click
import Files

def load():
    data=Files.load_from_json(Files.join_path(Files.current_path(),'.wit\dataJson.json'))
    return Repository.to_repository(data)
def save(rep):
    data = rep.to_dict()
    Files.save_to_json(data,Files.join_path(Files.current_path(),'.wit\dataJson.json'))



@click.command()
@click.argument('func',type=click.Choice(['wit init','wit add .','wit add','wit commit','wit log','wit status','wit checkout']))
@click.argument('value',type= str,required=False)
def cli(func,value):
    if func == 'wit init':
        rep = Repository()
        save(rep)
    else:
        rep = load()
        if func == 'wit add .':
            rep.wit_add(value)
        elif func == 'wit add':
            rep.wit_add()
        elif func == 'wit commit':
            rep.wit_commit(value)
        elif func == 'wit log':
            rep.wit_log()
        elif func == 'wit status':
            rep.wit_status()
        elif func == 'wit checkout':
            rep.wit_checkout(value)
    save(rep)

#לבדוק אם צריך להוסף מין