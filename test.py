slide:
    Voice:
    Breath:
    Pulse:
    Skin:
    Feel:
    Temp:
    Pain:
    Pain2:
    Bleed:
    Leak:
    Other:

<Voice>:
    question: question
    name: 'voice'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'describe patient's voice'

        GridLayout:
            cols:2
            Button:
                text:'A: croaky voice'
                on_press:
                    root.A()
                    app.root.current = 'breath'
            Button:
                text:'B: Difficulty speaking'
                on_press:
                    root.B()
                    app.root.current = 'breath'
            Button:
                text:'C: wheezing'
                on_press:
                    root.C()
                    app.root.current = 'breath'

            Button:
                text:'D: Normal'
                on_press:
                    root.D()
                    app.root.current = 'breath'

        TextInput:
            id: question
            multiline:False
        Button:
            text:'Submit written answer'
            on_press:
                root.check(question)
                app.root.current = 'breath'



<Breath>:
    question: question
    name: 'breath'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'describe the breath'

        GridLayout:
            cols:2
            Button:
                text:'A: Rapid'
                on_press:
                    root.A()
            Button:
                text:'B: Deep'
                on_press:
                    root.B()

            Button:
                text:'C: Gasping'
                on_press:
                    root.C()


            Button:
                text:'D: Normal'
                on_press:
                    root.D()
                    app.root.current = 'pulse'

        TextInput:
            id: question
            multiline:False
        Button:
            text:'Submit written answer'
            on_press:
                root.check(question)
                app.root.current = 'pulse'

<Pulse>:
    question: question
    name: 'pulse'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'describe the pulse'

        GridLayout:
            cols:2
            Button:
                text:'A: Fast'
                on_press:
                    root.A()
            Button:
                text:'B: Faint or weak'
                on_press:
                    root.B()
            Button:
                text:'C: None'
                on_press:
                    root.C()
                    app.root.current = 'skin'

            Button:
                text:'D: Normal'
                on_press:
                    root.D()
                    app.root.current = 'skin'

        TextInput:
            id: question
            multiline:False
        Button:
            text:'Submit written answer'
            on_press:
                root.check(question)
                app.root.current = 'skin'

<Skin>:
    question: question
    name: 'skin'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'describe the skin colour or face colour'

        GridLayout:
            cols:2
            Button:
                text:'A: Grey-Blue'
                on_press:
                    root.A()
            Button:
                text:'B: Red and puffy face'
                on_press:
                    root.B()
            Button:
                text:'C: Normal'
                on_press:
                    root.C()

                    app.root.current = 'feel'


            Button:
                text:'D: pale'
                on_press:
                    root.D()
        Button:
                text:'E: swelling'
                on_press:
                    root.E()

        TextInput:
            id: question
            multiline:False
        Button:
            text:'Submit written answer'
            on_press:
                root.check(question)

                app.root.current = 'feel'


<Feel>:
    question: question
    name: 'feel'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'how is patient feeling'

        GridLayout:
            cols:2
            Button:
                text:'A: Anxiety or alarm'
                on_press:
                    root.A()


            Button:
                text:'B: Faint'
                on_press:
                    root.B()


            Button:
                text:'C: Nausea or dizzy'
                on_press:
                    root.C()



            Button:
                text:'D: distress'
                on_press:
                    root.D()

            Button:
                text:'E: Normal'
                on_press:
                    root.E()
                    app.root.current = 'temp'
            Button:
                text:'F: Light headed or weak'
                on_press:
                    root.F()

        TextInput:
            id: question
            multiline:False
        Button:
            text:'Submit written answer'
            on_press:
                root.check(question)
                app.root.current = 'temp'

<Temp>:
    question:question
    name: 'temp'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'what is temperature of patient'

        GridLayout:
            cols:2
            Button:
                text:'A: Hot'
                on_press:
                    root.A()

                    app.root.current = 'pain'
            Button:
                text:'B: Cold'
                on_press:
                    root.B()
                    app.root.current = 'pain'
        Button:
            text: 'C: normal'
            on_press:
                root.C()
                app.root.current = 'pain'

<Pain>:
    name:'pain'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'does patient feel any pain'
        GridLayout:
            cols:2
            Button:
                text:'A: Yes'
                on_press:
                    app.root.current = 'pain2'
            Button:
                text:'B: No pain'
                on_press:
                    root.B()
                    app.root.current = 'bleed'

<Pain2>:
    question: question
    name: 'pain2'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'Where is pain'

        GridLayout:
            cols:2
            Button:
                text:'A: Headache'
                on_press:
                    root.A()

            Button:
                text:'B: Feeling of broken bone'
                on_press:
                    root.B()

            Button:
                text:'C: chest pain'
                on_press:
                    root.C()

            Button:
                text:'D: don't know where'
                on_press:
                    root.D()
                    app.root.current = 'bleed'

        Button:
            text:'E: on wound'
            on_press:
                root.E()
                app.root.current = 'bleed'

        TextInput:
            id: question
            multiline:False
        Button:
            text:'Submit written answer'
            on_press:
                root.check(question)
                app.root.current = 'bleed'



<Bleed>:
    question: question
    name: 'bleed'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'If there is visible blood describe it'

        GridLayout:
            cols:2
            Button:
                text:'A: _____'
                on_press:
                    root.A()

            Button:
                text:'B: _____'
                on_press:
                    root.B()

            Button:
                text:'C: Coughing blood'
                on_press:
                    root.C()


            Button:
                text:'D: No blood'
                on_press:
                    root.D()
                    app.root.current = 'leak'

        TextInput:
            id: question
            multiline:False
        Button:
            text:'Submit written answer'
            on_press:
                root.check(question)
                app.root.current = 'leak'


<Leak>:
    question: question
    name: 'leak'
    GridLayout:
        cols:1
        size: root.width, root.height
        Label:
            text: 'any other leaking other than blood'

        GridLayout:
            cols:2
            Button:
                text:'A: Vomiting'
                on_press:
                    root.A()

            Button:
                text:'B: Sweating'
                on_press:
                    root.B()

        Button:
            text:'C: None'
            on_press:
                root.C()
                app.root.current = 'other'
        TextInput:
            id: question
            multiline:False
        Button:
            text:'Submit written answer'
            on_press:
                root.check(question)
                app.root.current = 'other'


<Other>:
    name: 'other'
    Label:
        text: 'f'
