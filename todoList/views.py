from django.shortcuts import render, get_object_or_404
import pymongo
from .utils import get_db_handle
from django.http import HttpResponse
from bson.objectid import ObjectId
from django.conf import settings
from pprint import pprint

dbname, my_client = get_db_handle('todo_list','localhost',27017)
# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["todo_list_task"]

# Create your views here.
def create(request):
    title = request.POST.get('title',"Non défini")
    description = request.POST.get('description',"Non défini")
    etat = False
    #let's create two documents
    task= {
        "title": title,
        "description": description,
        "etat": etat,
    }
    # Insert the documents
    collection_name.insert_one(task)

    todo = collection_name.find()

    todolist = [{'id': str(td["_id"]), 'title' : td["title"], 'description' : td["description"], 'etat' : td["etat"]} for td in todo]

    nbTache = collection_name.count_documents({})
    nbTacheFini = collection_name.count_documents({"etat":True})
    nbTacheEnCours = collection_name.count_documents({"etat":False})
    return render(request, "list/create.html",{"todolist":todolist,
                                               "nbTache":nbTache,
                                               "nbTacheFini":nbTacheFini,
                                               "nbTacheEnCours":nbTacheEnCours,
                                               })
    
    return render(request, "list/create.html")

def read(request):
    todo = collection_name.find()

    todolist = [{'id': str(td["_id"]), 'title' : td["title"], 'description' : td["description"], 'etat' : td["etat"]} for td in todo]

    nbTache = collection_name.count_documents({})
    nbTacheFini = collection_name.count_documents({"etat":True})
    nbTacheEnCours = collection_name.count_documents({"etat":False})
    return render(request, "list/create.html",{"todolist":todolist,
                                               "nbTache":nbTache,
                                               "nbTacheFini":nbTacheFini,
                                               "nbTacheEnCours":nbTacheEnCours,
                                               })

def delete(request):

    choice = request.POST.get('delete').split(',')
    print(choice)
    for c in choice:
        collection_name.delete_one({"_id":ObjectId(c)})

    todo = collection_name.find()

    todolist = [{'id': str(td["_id"]), 'title' : td["title"], 'description' : td["description"], 'etat' : td["etat"]} for td in todo]

    nbTache = collection_name.count_documents({})
    nbTacheFini = collection_name.count_documents({"etat":True})
    nbTacheEnCours = collection_name.count_documents({"etat":False})
    return render(request, "list/create.html",{"todolist":todolist,
                                               "nbTache":nbTache,
                                               "nbTacheFini":nbTacheFini,
                                               "nbTacheEnCours":nbTacheEnCours,
                                               })


def update(request):
    id = ObjectId(request.POST.get('id'))
    task = [{'id': str(td["_id"]), 'title' : td["title"], 'description' : td["description"], 'etat' : td["etat"]} for td in collection_name.find({"_id":id})]
    print(task)
        
    return render(request,"list/modify.html",{"task":task})
    
def modify(request):
    id = ObjectId(request.POST.get('id'))
    title = request.POST.get('title')
    description = request.POST.get('description')
    etat = request.POST.get('etat') == 'true'
    
    collection_name.update_one({"_id": id},{"$set":{"title":title, "description":description, "etat":etat}})
    task = [{'id': str(td["_id"]), 'title' : td["title"], 'description' : td["description"], 'etat' : td["etat"]} for td in collection_name.find({"_id":id})]
    return render(request,"list/modify.html",{"task":task})

def achever(request):
    id = ObjectId(request.POST.get('achever'))

    collection_name.update_one({"_id":id},{"$set":{"etat" : True}})

    todo = collection_name.find()

    todolist = [{'id': str(td["_id"]), 'title' : td["title"], 'description' : td["description"], 'etat' : td["etat"]} for td in todo]

    nbTache = collection_name.count_documents({})
    nbTacheFini = collection_name.count_documents({"etat":True})
    nbTacheEnCours = collection_name.count_documents({"etat":False})
    return render(request, "list/create.html",{"todolist":todolist,
                                               "nbTache":nbTache,
                                               "nbTacheFini":nbTacheFini,
                                               "nbTacheEnCours":nbTacheEnCours,
                                               })
