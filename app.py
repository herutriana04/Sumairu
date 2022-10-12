from flask import Flask, render_template, request, redirect, url_for, session, flash
from rdkit import Chem
from rdkit.Chem import Draw
import random

def mol_with_atom_index(mol):
    for atom in mol.GetAtoms():
        atom.SetAtomMapNum(atom.GetIdx())
    return mol

app = Flask(__name__)

@app.route('/')
def test():
    return render_template("home.html")

@app.route('/draw')
def draw():
    return render_template("input.html")

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        mole = request.form['smile']
        n = random.randint(0,100000)
        mm = Chem.MolFromSmiles(mole)
        m = mol_with_atom_index(mm)
        filename = str(n)+".png"
        path = "static/uploads/"
        molFile = path+filename
        Draw.MolToFile(m,molFile)
        return render_template("result.html",mol=mole,MOLFILE=molFile)


if __name__ == '__main__':
    app.run(debug=True)