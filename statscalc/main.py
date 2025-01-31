import json

equipment = {
    'name':'',
    'rarity':0,
    'atkRate':0.0,
    'atk':0,
    'atk%':0.0,
    'hp':0,
    'hp%':0.0,
    'def':0,
    'def%':0.0,
    'aff':0.0,
    'evade':0.0,
    'atkSpd':0.0,
    'crtRate':0.0,
    'crtDmg':0.0,
    'lifeDrain':0.0,
    'fireAtk':0,
    'waterAtk':0,
    'earthAtk':0,
    'windAtk':0,
    'enemyFR':0.0,
    'enemyWaR':0.0,
    'enemyER':0.0,
    'enemyWiR':0.0,
    'fR':0.0,
    'waR':0.0,
    'eR':0.0,
    'wiR':0.0,
    'darkR':False,
    'stunR':False,
    'freezeR':False,
    'weakenR':False,
    'dark':0.0,
    'stun':0.0,
    'freeze':0.0,
    'weaken':0.0,
    'enemyAtk':0.0,
    'enemyDef':0.0,
    'essenceGain':0.0,
    'recoverEvade':0.0
}

daggers = []
swords = []
hammers = []

print(equipment)

def createNewEquipment():
    newEquipment = equipment
    for ind in newEquipment:
        newEquipment[ind] = input(f'Inserisci il valore per {ind}:')
    return newEquipment

def insertNewDagger(daggerEquip):
    daggers.append(daggerEquip)

def getDaggers():
    for dagger in daggers:
        print(dagger)
        return(dagger)

def saveOnDaggers(daggers):
    path = './statscalc/data/daggers.json'
    oldData = getOldData(path)
    #newData = 
    with open(path, 'w') as fp:
        json.dumps(daggers, fp, indent=2)

def test(daggers):
    path = './statscalc/data/daggers.json'
    with open(path, 'a') as fp:
        json.dump(daggers, fp, indent=2)

def getOldData(path):
    with open(path, 'r') as fp:
        data = json.loads(fp)
    return data

insertNewDagger(createNewEquipment())

test(getDaggers())