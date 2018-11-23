#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:40:12 2018

@author: chia
"""

import gtk

# Ventana Alineamiento Simple
class anotherWinAlign(gtk.Window):
    def __init__(self):   
        ############################
        #          Ventana         #
        ############################        
        super(anotherWinAlign,self).__init__()
        # llamando al evento on_destroy 
        self.connect("destroy",self.on_destroy)
        self.set_default_size(960,960)   # x,y
        # titulo de la ventana 
        self.set_title("Alineamiento Simple")
        
        # modificar el tamano de screen 
        screen = gtk.Fixed()
        
        #####################################
        #    Elegir el tipo de secuencia    #
        #####################################
        tipo = gtk.Label()
        tipo.set_markup("<b>Selecciona el tipo de secuencia:</b>")
        #ComoboxTex para elegir el tipo de  secuencia
        self.tipo_combobox = gtk.combo_box_new_text()
         # llamando al evento on_changed_tipo 
        self.tipo_combobox.connect("changed",self.on_changed_tipo) 
        self.tipo_combobox.append_text("Gen")
        self.tipo_combobox.append_text("Proteína")
        
        ############################
        #        Secuencia1        #
        ############################
        seq1 = gtk.Label() 
        seq1.set_markup("<b>Selecciona la primera secuencia:</b>")
        ########## PAISES
        pais_seq1 = gtk.Label()
        pais_seq1.set_markup("<b>País</b>")
        # ComoboxTex para elegir el pais
        self.selec_pais_seq1 = gtk.combo_box_new_text() 
        self.selec_pais_seq1.connect("changed",self.on_changed_pais_seq1) 
        # Items del combobox (paises disponibles)
        self.selec_pais_seq1.append_text("Argentina")
        self.selec_pais_seq1.append_text("Australia")
        self.selec_pais_seq1.append_text("Brasil")
        self.selec_pais_seq1.append_text("China")
        self.selec_pais_seq1.append_text("Colombia")
        self.selec_pais_seq1.append_text("Filipinas")
        self.selec_pais_seq1.append_text("India")
        self.selec_pais_seq1.append_text("Indonesia")
        self.selec_pais_seq1.append_text("Jamaica")
        self.selec_pais_seq1.append_text("Madagascar")
        self.selec_pais_seq1.append_text("México")
        self.selec_pais_seq1.append_text("Srilanka")
        self.selec_pais_seq1.append_text("Tailandia")
        self.selec_pais_seq1.append_text("Uruguay")

        ########## ESPECIES
        especie_seq1 = gtk.Label()
        especie_seq1.set_markup("<b>Especie</b>")
        # ComoboxTex para elegir la especie
        self.selec_especie_seq1 = gtk.combo_box_new_text()
        self.selec_especie_seq1.connect("changed",self.on_changed_especie_seq1) 
        # Items del combobox (especies disponibles, inicialmente vacio)
        self.selec_especie_seq1.append_text("------")
        
        ########## IDs DE LAS SECUENCIAS
        ids_seq1 = gtk.Label()
        ids_seq1.set_markup("<b>Selecciona un id:</b>")
        #treeView para elegir el ID
        # se muestra una lista 
        treeView = gtk.TreeView()
        treeView.connect("row-activated", self.on_activated_seq1)
        # Items de los IDs (IDs disponibles, inicialmente vacio)
        self.store_ids = gtk.ListStore(str)
        self.store_ids.append(["----------------------"])
        treeView.set_model(self.store_ids)
        # Columnas 
        rendererText = gtk.CellRendererText()
        rendererText.set_property('editable',True)
        rendererText.set_property('cell-background','#819FF7')
        column = gtk.TreeViewColumn("Secuencias\nDisponibles", rendererText, text=0)
        treeView.append_column(column)
        treeView.set_headers_visible(False)
        treeView.set_enable_search(True)
        #scrolledwindow = gtk.ScrolledWindow()
        #scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        #scrolledwindow.add_with_viewport(treeView)
        
        

        ############################
        #        Secuencia2        #
        ############################
        seq2 = gtk.Label("Selecciona la segunda secuencia: ")
        
        
        ############################
        #        screen.put        #
        ############################
        # tipo de secuencia
        screen.put(tipo,50,25)
        screen.put(self.tipo_combobox,280,20) # ComboboxText
        
        # secuencia 1
        screen.put(seq1,50,85) # mensaje secuencia1
        # secuencia 1: pais
        screen.put(pais_seq1,50,120) # mensaje pais
        screen.put(self.selec_pais_seq1,90,110) # ComboboxText pais
        # secuencia 1: especie
        screen.put(especie_seq1,300,120) # mensaje especie
        screen.put(self.selec_especie_seq1,370,110) # ComboboxText especie
        # secuencia 1: IDs 
        screen.put(ids_seq1, 50,170) # mensaje IDs
        screen.put(treeView, 50,200) # treeView IDs
        # secuencia 2
        #screen.put(seq2,50,450) # mensaje secuencia2
        
        ############################
        #          Ventana         #
        ############################                   
        self.add(screen)
        self.show_all()
        

    def on_destroy(self,widget):
        widget.hide()
        
    def on_changed_tipo(self,widget):
        self.store_ids.clear()
        self.store_ids.append(["----------------------"])
        self.selec_pais_seq1.set_active(-1)
        self.selec_especie_seq1.set_active(-1)

    def on_changed_pais_seq1(self,widget):
        text_pais_seq1 = widget.get_active_text()
        print(text_pais_seq1)
        if (text_pais_seq1 == "Argentina"):
            self.selec_especie_seq1.get_model().clear()
            bd_argen= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Argentina','r')
            for item in bd_argen.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Australia"):
            self.selec_especie_seq1.get_model().clear()
            bd_austr= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Australia','r')
            for item in bd_austr.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Brasil"): 
            self.selec_especie_seq1.get_model().clear()
            bd_brasil= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Brasil','r')
            for item in bd_brasil.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "China"):
            self.selec_especie_seq1.get_model().clear()
            bd_chi= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_China','r')
            for item in bd_chi.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Colombia"): 
            self.selec_especie_seq1.get_model().clear()
            bd_colo= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Colombia','r')
            for item in bd_colo.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Filipinas"):
            self.selec_especie_seq1.get_model().clear()
            bd_fili= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Filipinas','r')
            for item in fili.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "India"): 
            self.selec_especie_seq1.get_model().clear()
            bd_indi= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_India','r')
            for item in bd_indi.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Indonesia"):
            self.selec_especie_seq1.get_model().clear()
            bd_indo= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Indonesia','r')
            for item in bd_indo.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Jamaica"): 
            self.selec_especie_seq1.get_model().clear()
            bd_jama= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Jamaica','r')
            for item in bd_jama.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Madagascar"):
            self.selec_especie_seq1.get_model().clear()
            bd_mada= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Madagascar','r')
            for item in bd_mada.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "México"): 
            self.selec_especie_seq1.get_model().clear()
            bd_mex= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Mexico','r')
            for item in bd_mex.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Srilanka"):
            self.selec_especie_seq1.get_model().clear()
            bd_sri= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Srilanka','r')
            for item in bd_sri.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Tailandia"): 
            self.selec_especie_seq1.get_model().clear()
            bd_tai= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Tailandia','r')
            for item in bd_tai.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Uruguay"):
            self.selec_especie_seq1.get_model().clear()
            bd_uru= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Uruguay','r')
            for item in bd_uru.readlines():
                self.selec_especie_seq1.append_text(item)

    def on_changed_especie_seq1(self,widget):
        # tipo 1 sera el valor seleccionado del tipo ya sea gen o proteina 
        tipo1 = self.tipo_combobox.get_active_text()
        # pais1 sera el pais escogido 
        pais1 = self.selec_pais_seq1.get_active_text()
        # especie1 sera la especie escogida con respecto a su pais  
        especie1 = self.selec_especie_seq1.get_active_text()
        if tipo1 == "Gen":
            if (pais1 =="Argentina"):
                # bd_argen, guarda la lista de las especies de Argentina 
                bd_argen= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Argentina','r')
                for item in bd_argen.readlines():
                    # name guardara el valor que hay en item 
                    name= item
                    # actualiza el valor de item solo que no toma el salto de linea  
                    name = name[:len(name)-1]
                    # archivo es la direccion de los ids de los genes de una especie 
                    archivo= '/home/alexandra/Escritorio/Argentina'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        # bd_argen2 guardara los ids de los genes de una especie 
                        bd_argen2= open(archivo,'r')
                        for item2 in bd_argen2:
                            # se agrega uno por uno de los ids a la lista 
                            self.store_ids.append ([item2])
               
            elif (pais1 =="Australia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Australia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= '/home/alexandra/Escritorio/Australia'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
        elif tipo1 == "Proteína":
            if (pais1 =="Argentina"):
                bd_argen= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Argentina','r')
                for item in bd_argen.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= '/home/alexandra/Escritorio/Argentina'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_argen2= open(archivo,'r')
                        for item2 in bd_argen2:
                            self.store_ids.append ([item2])
               
            elif (pais1 =="Australia"):
                bd_aus= open('/home/alexandra/Escritorio/Paises_selec/fauna_endemica_Australia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= '/home/alexandra/Escritorio/Australia'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in aus2:
                            self.store_ids.append ([item2])

            
    def on_activated_seq1(self, widget, row, col):
        model = widget.get_model()
        current_id = model[row][0]
        print(current_id)
        '''
        if current_id == "----------------------":
            self.store_ids.clear()
            self.store_ids.append (["A.123"])
            self.store_ids.append (["A.15615"])
            self.store_ids.append (["A.515"])
            self.store_ids.append (["A.4555"])
            self.store_ids.append (["A.515415"])
        '''
        
            

# Ventana Alineamiento Multiple
class anotherWinAlignM(gtk.Window):
    def __init__(self):   
        ############################
        #          Ventana         #
        ############################        
        super(anotherWinAlignM,self).__init__()
        self.connect("destroy",self.on_destroy)
        self.set_default_size(960,960)
        self.set_title("Alineamiento Múltiple")
        self.add(gtk.Label("This is another window"))
        self.show_all()
        
    def on_destroy(self,widget):
        widget.hide()
        
# Ventana Arbol Filogenetico
class anotherWinTree(gtk.Window):
    def __init__(self):   
        ############################
        #          Ventana         #
        ############################        
        super(anotherWinTree,self).__init__()
        self.connect("destroy",self.on_destroy)
        self.set_default_size(960,960)
        self.set_title("Árbol Filogenético")
        self.add(gtk.Label("This is another window"))
        self.show_all()
        
    def on_destroy(self,widget):
        widget.hide()
        
class PyApp(gtk.Window):
    def __init__(self):
        # creando la ventana
        super(PyApp,self).__init__()
        self.set_default_size(320,240)
        self.set_title("My Biology App")
        self.set_position(gtk.WIN_POS_CENTER)
        # Primer boton
        align = gtk.Button("Alineamiento Simple")
        #crear a gdk.color para el color del boton  
        map = align.get_colormap() 
        color = map.alloc_color("#81F79F") 
        #copiar el estilo actual y reemplazarlo 
        style = align.get_style().copy()
        style.bg[gtk.STATE_NORMAL] = color 
        #cambiar el estilo del boton por el estilo escogido  
        align.set_style(style)         

        align.connect("clicked",self.align_Event)
        align.set_size_request(200,40)
        
        # Segundo boton
        alignM = gtk.Button("Alineamiento Múltiple")
        #crear a gdk.color para el color del boton  
        map = alignM.get_colormap() 
        color = map.alloc_color("#9F81F7") 
        #copiar el estilo actual y reemplazarlo 
        style = alignM.get_style().copy()
        style.bg[gtk.STATE_NORMAL] = color 
        #cambiar el estilo del boton por el estilo escogido  
        alignM.set_style(style)  
        alignM.connect("button_press_event",self.alignM_Event)
        alignM.set_size_request(200,40)

        # Tercer Boton
        tree = gtk.Button("Árbol Filogenético")
        #crear a gdk.color para el color del boton  
        map = tree.get_colormap() 
        color = map.alloc_color("#FA8258") 
        #copiar el estilo actual y reemplazarlo 
        style = tree.get_style().copy()
        style.bg[gtk.STATE_NORMAL] = color 
        #cambiar el estilo del boton por el estilo escogido  
        tree.set_style(style)  
        tree.connect("button_press_event",self.tree_Event)
        tree.set_size_request(200,40)
        
        screen = gtk.Fixed()
        
        message = gtk.Label()
        message.set_markup("<b><big>¡Bienvenido a My Biology App!</big></b>")
        screen.put(message,25,25)
        
        message2= gtk.Label()
        message2.set_markup("<b>Selecciona una opción:</b>")
        screen.put(message2,25,70)
        
        screen.put(align,65,100)
        screen.put(alignM,65,140)
        screen.put(tree,65,180)
        
        self.add(screen)


    def align_Event(self,win):
        print("Alineamiento Simple!!")
        align_Win = anotherWinAlign()
        
    def alignM_Event(self,widget,event):
        print("Alineamiento Múltiple!!")
        alignM_Win = anotherWinAlignM()

    
    def tree_Event(self,widget,event):
        print("Árbol Filogenético!!")
        tree_Win = anotherWinTree()


window = PyApp()
window.connect("destroy",gtk.main_quit)
window.show_all()
gtk.main()
