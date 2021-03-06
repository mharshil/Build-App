import kivy
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen



Hypoxia = ['rapid breath','gasping','difficulty speaking','grey-blue skin','anxiety','restlessness','headache','nausea','vomiting','Pn','Tn']
Airway_Obstruction = ['rapid breath','gasping','difficulty speaking','grey-blue skin','red and puffy face','persistent','flaring nostrils','Pn','Tn','no pain','Ln']
Hyperventilation = ['deep breath','fast breath','fast pulse','anxiety','faint','dizzy','dry mouth','Sn','Tn','no pain','speak','Ln']
Asthma = ['wheezing','anxiety','coughing','distress','gasping','grey-blue skin','exhaustion','Pn','Tn','no pain','Ln']
Croup = ['croaky voice','blue-grey skin','coughing','Bn','Pn','Tn','no pain','Ln']
Penetrating_Chest_Wound = ['gasping','cough blood','anxiety','grey-blue ski ','rapid breath','Pn','Tn','chest pain','Ln']
Shock = ['sweat','cold','pale','fast pulse','Bn','Ln','no pain','speak']
Internal_Bleeding = ['pale','cold','faint pulse','fast pulse','thirsty','confused','pain','Ln','rapid breath','blue-grey skin','speak']
Infected_wound = ['pain on wound','pus','red-trail skin','swelling','Pn','Bn','Tn','speak']
Fracture = ['broken bone','pain on wound','swelling','fast pulse','cold','sweat','pale','Bn','Ln','speak']
Burns_To_Airway = ['difficulty breathing','croaky voice','swelling','Pn','Tn','Ln']
Dehydration = ['confusion','nausea','Headache','dry skin','cracked lips','Pn','Bn','Tn','speak','no pain','dark urine','Ln']
Heat_Stroke = ['headache','nausea','restlessness','confusion','dry skin','hot','fast pulse','Bn','speak','Ln','impaired response']
Hypothermia = ['cold','pale','shivering','shallow breath','slow breath','impaired response','Pn','speak','Ln',]
Heart_Attack = ['gasping','fast pulse','faint pulse','sweat','chest pain','Tn','Ln','ashen skin','faint','nausea','speak']
Stroke = ['light headed','nausea','difficulty speaking','confusion','impaired response','blurred vision','Pn','Ln','Bn','Tn']


Disease = [Hypoxia,Airway_Obstruction,Hyperventilation,Asthma,Croup,Penetrating_Chest_Wound,Shock,Internal_Bleeding,Infected_wound,Fracture,Burns_To_Airway,Dehydration,Heat_Stroke,Hypothermia,Heart_Attack]

names = ['Hypoxia','Airway_Obstruction','Hyperventilation','Asthma','Croup','Penetrating_Chest_Wound','Shock','Internal_Bleeding','Infected_wound','Fracture','Burns_To_Airway','Dehydration','Heat_Stroke','Hypothermia','Heart_Attack']
global not_in
not_in = 0
chances = []

for x in range (0,len(Disease)):
  chances.append(0)

#--------------------------------------------------------------------

class Voice(Screen):
    question = ObjectProperty(None)

    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)

    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'croaky voice' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'difficulty speaking' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'wheezing' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def D(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'speak' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)



#------------------------------------------------------------------

class Breath(Screen):
    question = ObjectProperty(None)
    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)
    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'rapid breath' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'deep breath' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'gasping' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def D(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'Bn' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)



#----------------------------------------------------------

class Pulse(Screen):
    question = ObjectProperty(None)
    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)
    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'fast pulse' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'faint pulse' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'none' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def D(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'Pn' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)



#--------------------------------------------------------

class Skin(Screen):
    question = ObjectProperty(None)

    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)

    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'grey-blue skin' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'red and puffy face' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'Sn' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def D(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'pale' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def E(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'swelling' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)


#----------------------------------------------------


class Feel(Screen):
    question = ObjectProperty(None)

    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)

    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'anxiety' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'faint' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'nausea' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def D(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'distress' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def E(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'Fn' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def F(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'light headed' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)



#----------------------------------------------------------


class Temp(Screen):
    question = ObjectProperty(None)

    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)

    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'hot' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'cold' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'Tm' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)


#----------------------------------------------------------

class Pain(Screen):
    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'no pain' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)


class Pain2(Screen):
    question = ObjectProperty(None)

    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)

    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'headache' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'broken bone' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'chest pain' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def D(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'pain' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def E(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'pain on wound' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)


#------------------------------------------------------------

class Response(Screen):
    question = ObjectProperty(None)

    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)

    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'blurred vision' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'impaired response' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'confusion' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def D(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'Fn' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)


#-------------------------------------------------------------


class Leak(Screen):
    def check(self, question):
        global not_in
        for x in range(0, len(Disease)):
            if self.question.text in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
        print(self.question.text)

    def A(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'sweat' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

    def B(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'vomiting' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def C(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'Ln' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)
    def D(self):
        global not_in
        for x in range(0, len(Disease)):
            if 'Ln' in Disease[x]:
                chances[x] = chances[x] + 1
            else:
                chances[x] = chances[x]
                not_in = not_in + 1
        print(chances)

#------------------------------------------------------------


class Other(Screen):
    pass

#------------------------------------------------------------

class slide(ScreenManager):
    pass


kv = Builder.load_file('my.kv')

class my(App):
    def build(self):
        return kv

if __name__ == "__main__":
    my().run()