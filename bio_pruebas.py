#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:40:12 2018

@author: chia
"""

import gtk
tipo=""
pais1 = ""
especie1= ""
numId= ""

# Ventana para mostrar fastas 
class WinFasta(gtk.Window):
    def __init__(self):   
        ############################
        #          Ventana         #
        ############################        
        super(WinFasta,self).__init__()
        # llamando al evento on_destroy 
        self.connect("destroy",self.on_destroy)
        self.set_default_size(500,400)   # size en formato x,y
        # titulo de la ventana
        nombre = tipo + '_'+ especie1 + '_' + numId + '.fasta'
        self.set_title(nombre)

    def on_destroy(self,widget):
        widget.hide()


# Ventana Alineamiento Simple
class anotherWinAlign(gtk.Window):
    def __init__(self):   
        ############################
        #          Ventana         #
        ############################        
        super(anotherWinAlign,self).__init__()
        # llamando al evento on_destroy 
        self.connect("destroy",self.on_destroy)
        self.set_default_size(960,960)   # size en formato x,y
        # titulo de la ventana 
        self.set_title("Alineamiento Simple")
        

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
        
        ########## PAIS
        pais_seq1 = gtk.Label()
        pais_seq1.set_markup("<b>País:</b>")
        
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

        ########## ESPECIE
        especie_seq1 = gtk.Label()
        especie_seq1.set_markup("<b>Especie:</b>")
        
        # ComoboxTex para elegir la especie
        self.selec_especie_seq1 = gtk.combo_box_new_text()
        self.selec_especie_seq1.connect("changed",self.on_changed_especie_seq1) 
        # Items del combobox (especies disponibles, inicialmente vacio)
        self.selec_especie_seq1.append_text("------")
        
        ########## IDs DE LAS SECUENCIAS
        ids_seq1 = gtk.Label()
        ids_seq1.set_markup("<b>Selecciona un id haciendo doble click sobre él:</b>")
        
        # treeView para elegir el ID 
        treeView = gtk.TreeView()
        treeView.connect("row-activated", self.on_activated_seq1)
        
        # Items de los IDs (IDs disponibles, inicialmente vacio)
        self.store_ids = gtk.ListStore(str)
        self.store_ids.append(["----------------------"])
        treeView.set_model(self.store_ids)
        
        # Columna
        rendererText = gtk.CellRendererText()
        #rendererText.set_property('editable',True)
        #rendererText.set_property('cell-background','#819FF7')
        column = gtk.TreeViewColumn("Secuencias\nDisponibles", rendererText, text=0)
        
        # Agregando la columna al treeView
        treeView.append_column(column)
        treeView.set_headers_visible(False)
        treeView.set_enable_search(True)

        # ScrolledWindow
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.add(treeView)
    

        ############################
        #        Secuencia2        #
        ############################
        seq2 = gtk.Label()
        seq2.set_markup("<b>Selecciona la segunda secuencia:</b>")

        ########## PAIS
        pais_seq2 = gtk.Label()
        pais_seq2.set_markup("<b>País:</b>")

        # ComoboxTex para elegir el pais
        self.selec_pais_seq2 = gtk.combo_box_new_text()
        self.selec_pais_seq2.connect("changed",self.on_changed_pais_seq2)
        # Items del combobox (paises disponibles)
        self.selec_pais_seq2.append_text("Argentina")
        self.selec_pais_seq2.append_text("Australia")
        self.selec_pais_seq2.append_text("Brasil")
        self.selec_pais_seq2.append_text("China")
        self.selec_pais_seq2.append_text("Colombia")
        self.selec_pais_seq2.append_text("Filipinas")
        self.selec_pais_seq2.append_text("India")
        self.selec_pais_seq2.append_text("Indonesia")
        self.selec_pais_seq2.append_text("Jamaica")
        self.selec_pais_seq2.append_text("Madagascar")
        self.selec_pais_seq1.append_text("México")
        self.selec_pais_seq2.append_text("Srilanka")
        self.selec_pais_seq2.append_text("Tailandia")
        self.selec_pais_seq1.append_text("Uruguay")

        ########## ESPECIE
        especie_seq2 = gtk.Label()
        especie_seq2.set_markup("<b>Especie:</b>")

        # ComoboxTex para elegir la especie
        self.selec_especie_seq2 = gtk.combo_box_new_text()
        self.selec_especie_seq2.connect("changed",self.on_changed_especie_seq2)
        # Items del combobox (especies disponibles, inicialmente vacio)
        self.selec_especie_seq2.append_text("------")

        ########## IDs DE LAS SECUENCIAS
        ids_seq2 = gtk.Label()
        ids_seq2.set_markup("<b>Selecciona un id haciendo doble click sobre él:</b>")

        # treeView para elegir el ID
        treeView_seq2 = gtk.TreeView()
        treeView_seq2.connect("row-activated", self.on_activated_seq2)

        # Items de los IDs (IDs disponibles, inicialmente vacio)
        self.store_ids_seq2 = gtk.ListStore(str)
        self.store_ids_seq2.append(["----------------------"])
        treeView_seq2.set_model(self.store_ids_seq2)

        # Columna
        rendererText_seq2 = gtk.CellRendererText()
        #rendererText_seq2.set_property('editable',True)
        #rendererText_seq2.set_property('cell-background','#819FF7')
        column_seq2 = gtk.TreeViewColumn("Secuencias\nDisponibles", rendererText_seq2, text=0)

        # Agregando la columna al treeView
        treeView_seq2.append_column(column_seq2)
        treeView_seq2.set_headers_visible(False)
        treeView_seq2.set_enable_search(True)

        # ScrolledWindow
        scrolled_window_seq2 = gtk.ScrolledWindow()
        scrolled_window_seq2.add(treeView_seq2)

        #############################
        #  Align: tipo y parametros #
        #############################

        mensaje_tipo = gtk.Label("Selecciona el tipo de alineamiento: ")
        self.combobox_align_type = gtk.combo_box_new_text()
        self.combobox_align_type.append_text("Local")
        self.combobox_align_type.append_text("Global")

        ###################################
        #  Boton Align: tipo y parametros #
        ###################################
        
        mensaje_alignB = gtk.Label("Presiona para alinear")
        self.align_But = gtk.Button("Alinear")
        self.align_But.connect("clicked",self.align_ButEvent)
        
        

        #####################################################
        #     VBox para la primera parte de la ventana      #
        #####################################################

        # Hbox para seleccionar el tipo de secuencia
        # contiene el mensaje de "selecciona el tipo...."
        # y el combobox del tipo de secuencia
        box_tipo_seq = gtk.HBox()
        box_tipo_seq.pack_start(tipo,expand=False, fill=False, padding =30) # mensaje de "seleccionar..."
        box_tipo_seq.pack_start(self.tipo_combobox,expand=False, fill=False) # combobox del tipo de secuencia

        # Hbox para el mensaje de "selecciona la primera secuencia"
        box_mensaje_seleccion_seq1 = gtk.HBox()
        box_mensaje_seleccion_seq1.pack_start(seq1, expand=False, fill=False, padding =30)

        # Hbox para el mensaje "pais" y el combobox del pais de la seq1
        box_pais_seq1 = gtk.HBox()
        box_pais_seq1.pack_start(pais_seq1,expand=False, fill=False,padding =30)
        box_pais_seq1.pack_start(self.selec_pais_seq1,expand=False,fill=False)

        # Hbox para el mensaje "especie" y el combobox de la especie de la seq1
        box_especie_seq1 = gtk.HBox()
        box_especie_seq1.pack_start(especie_seq1,expand=False, fill=False,padding =30)
        box_especie_seq1.pack_start(self.selec_especie_seq1,expand=False, fill=False)

        # Hbox para el pais y especie de la seq1
        box_pais_especie_seq1 = gtk.HBox()
        box_pais_especie_seq1.pack_start(box_pais_seq1,expand=False, fill=False)
        box_pais_especie_seq1.pack_start(box_especie_seq1,expand=False, fill=False, padding = 150)

        # Hbox para el mensaje "Selecciona un id"
        box_mensaje_seleccion_id = gtk.HBox()
        box_mensaje_seleccion_id.pack_start(ids_seq1,expand=False, fill=False, padding =30)

        # Hbox para la lista de IDs
        box_id_list = gtk.HBox()
        box_id_list.pack_start(scrolled_window, padding =30)

        box_parte1 = gtk.VBox()
        box_parte1.pack_start(box_tipo_seq,expand=False, fill=False, padding =30)
        box_parte1.pack_start(box_mensaje_seleccion_seq1, expand=False, fill=False)
        box_parte1.pack_start(box_pais_especie_seq1,expand=False, fill=False, padding =20)
        box_parte1.pack_start(box_mensaje_seleccion_id,expand=False, fill=False)
        box_parte1.pack_start(box_id_list,padding=10)


        #####################################################
        #     VBox para la segunda parte de la ventana      #
        #####################################################
        # Hbox para el mensaje de "selecciona la segunda secuencia"        
        box_mensaje_seleccion_seq2 = gtk.HBox()
        box_mensaje_seleccion_seq2.pack_start(seq2, expand=False, fill=False, padding =30)

        # Hbox para el mensaje "pais" y el combobox del pais de la seq2
        box_pais_seq2 = gtk.HBox()
        box_pais_seq2.pack_start(pais_seq2,expand=False, fill=False,padding =30)
        box_pais_seq2.pack_start(self.selec_pais_seq2,expand=False,fill=False)

        # Hbox para el mensaje "especie" y el combobox de la especie de la seq1
        box_especie_seq2 = gtk.HBox()
        box_especie_seq2.pack_start(especie_seq2,expand=False, fill=False,padding =30)
        box_especie_seq2.pack_start(self.selec_especie_seq2,expand=False, fill=False)

        # Hbox para el pais y especie de la seq1
        box_pais_especie_seq2 = gtk.HBox()
        box_pais_especie_seq2.pack_start(box_pais_seq2,expand=False, fill=False)
        box_pais_especie_seq2.pack_start(box_especie_seq2,expand=False, fill=False, padding = 150)

        # Hbox para el mensaje "Selecciona un id"
        box_mensaje_seleccion_id_seq2 = gtk.HBox()
        box_mensaje_seleccion_id_seq2.pack_start(ids_seq2,expand=False, fill=False, padding =30)

        # Hbox para la lista de IDs
        box_id_list_seq2 = gtk.HBox()
        box_id_list_seq2.pack_start(scrolled_window_seq2, padding =30)

        box_parte2 = gtk.VBox()
        box_parte2.pack_start(box_mensaje_seleccion_seq2, expand=False, fill=False)
        box_parte2.pack_start(box_pais_especie_seq2,expand=False, fill=False, padding =20)
        box_parte2.pack_start(box_mensaje_seleccion_id_seq2,expand=False, fill=False)
        box_parte2.pack_start(box_id_list_seq2,padding=10)

        #####################################################
        #     VBox para la tercera parte de la ventana      #
        #####################################################
        box_tipo_align = gtk.HBox()
        box_tipo_align.pack_start(mensaje_tipo,expand=False, fill=False,padding =30)
        box_tipo_align.pack_start(self.combobox_align_type,expand=False, fill=False)
        
        box_parte3 = gtk.VBox()
        box_parte3.pack_start(box_tipo_align,expand=False, fill=False)

        #####################################################
        #     VBox para la cuarta parte de la ventana      #
        #####################################################

        # Hbox para el boton alinear
        box_alignB = gtk.HBox()
        box_alignB.pack_start(mensaje_alignB,expand=False, fill=False,padding =30)
        box_alignB.pack_start(self.align_But,expand=False, fill=False)

        
        box_parte3.pack_start(box_alignB,expand=False, fill=False)

        #####################################################
        #            VBox principal de la ventana           #
        #####################################################
        box_main = gtk.VBox(spacing=10)
        box_main.pack_start(box_parte1)
        box_main.pack_start(box_parte2)
        box_main.pack_start(box_parte3)
        self.add(box_main)

        
        #######################################
        #   Mostrar elementos de la ventana   #
        #######################################                   
        self.show_all()
        

    def on_destroy(self,widget):
        widget.hide()
    

    # Funcion para la senal del boton alinear
    def align_ButEvent(self,widget):
        tipo_align= self.combobox_align_type.get_active_text()
        #print(tipo_align)
        if (tipo_align == "Local"):
            print(tipo_align)   # pasar el codigo alinear local con el id para recibir un fasta 
        elif (tipo_align == "Global"): 
            print(tipo_align)   # pasar el codigo alinear global con el id para recibir un fasta 
        
        

    
    def on_changed_tipo(self,widget):
        self.store_ids.clear()
        self.store_ids.append(["----------------------"])
        self.store_ids_seq2.clear()
        self.store_ids_seq2.append(["----------------------"])
        self.selec_pais_seq1.set_active(-1)
        self.selec_especie_seq1.set_active(-1)
        self.selec_pais_seq2.set_active(-1)
        self.selec_especie_seq2.set_active(-1)

    # Mostrar especies de un pais, para la primera secuencia 
    def on_changed_pais_seq1(self,widget):
        text_pais_seq1 = widget.get_active_text()
        print(text_pais_seq1)
        if (text_pais_seq1 == "Argentina"):
            self.selec_especie_seq1.get_model().clear()
            bd_argen= open('Paises_selec/fauna_endemica_Argentina','r')
            for item in bd_argen.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Australia"):
            self.selec_especie_seq1.get_model().clear()
            bd_austr= open('Paises_selec/fauna_endemica_Australia','r')
            for item in bd_austr.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Brasil"): 
            self.selec_especie_seq1.get_model().clear()
            bd_brasil= open('Paises_selec/fauna_endemica_Brasil','r')
            for item in bd_brasil.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "China"):
            self.selec_especie_seq1.get_model().clear()
            bd_chi= open('Paises_selec/fauna_endemica_China','r')
            for item in bd_chi.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Colombia"): 
            self.selec_especie_seq1.get_model().clear()
            bd_colo= open('Paises_selec/fauna_endemica_Colombia','r')
            for item in bd_colo.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Filipinas"):
            self.selec_especie_seq1.get_model().clear()
            bd_fili= open('Paises_selec/fauna_endemica_Filipinas','r')
            for item in bd_fili.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "India"): 
            self.selec_especie_seq1.get_model().clear()
            bd_indi= open('Paises_selec/fauna_endemica_India','r')
            for item in bd_indi.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Indonesia"):
            self.selec_especie_seq1.get_model().clear()
            bd_indo= open('Paises_selec/fauna_endemica_Indonesia','r')
            for item in bd_indo.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Jamaica"): 
            self.selec_especie_seq1.get_model().clear()
            bd_jama= open('Paises_selec/fauna_endemica_Jamaica','r')
            for item in bd_jama.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Madagascar"):
            self.selec_especie_seq1.get_model().clear()
            bd_mada= open('Paises_selec/fauna_endemica_Madagascar','r')
            for item in bd_mada.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Srilanka"):
            self.selec_especie_seq1.get_model().clear()
            bd_sri= open('Paises_selec/fauna_endemica_Srilanka','r')
            for item in bd_sri.readlines():
                self.selec_especie_seq1.append_text(item)
        elif (text_pais_seq1 == "Tailandia"): 
            self.selec_especie_seq1.get_model().clear()
            bd_tai= open('Paises_selec/fauna_endemica_Tailandia','r')
            for item in bd_tai.readlines():
                self.selec_especie_seq1.append_text(item)
       
    # Se muestra los ids de la especie escogida por la primera secuencia  
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
                bd_argen= open('Paises_selec/fauna_endemica_Argentina','r')
                for item in bd_argen.readlines():
                    # name guardara el valor que hay en item 
                    name= item
                    # actualiza el valor de item solo que no toma el salto de linea  
                    name = name[:len(name)-1]
                    # archivo es la direccion de los ids de los genes de una especie 
                    archivo= 'Argentina'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        # bd_argen2 guardara los ids de los genes de una especie 
                        bd_argen2= open(archivo,'r')
                        for item2 in bd_argen2:
                            # se agrega uno por uno de los ids a la lista 
                            self.store_ids.append ([item2])
               
            elif (pais1 =="Australia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Australia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Australia'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
             
            elif (pais1 =="Brasil"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Brasil','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Brasil'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
            
            elif (pais1 =="China"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_China','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'China'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Colombia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Colombia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Colombia'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Filipinas"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Filipinas','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Filipinas'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="India"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_India','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'India'+'/'+name+ '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Indonesia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Indonesia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Indonesia'+'/'+name +'_/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Jamaica"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Jamaica','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Jamaica'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
            
            elif (pais1 =="Madagascar"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Madagascar','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Madagascar'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Srilanka"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Srilanka','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Srilanka'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Tailandia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Tailandia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Tailandia'+'/'+name + '/'+ name+'_GENES'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
        elif tipo1 == "Proteína":
            if (pais1 =="Argentina"):
                # bd_argen, guarda la lista de las especies de Argentina 
                bd_argen= open('Paises_selec/fauna_endemica_Argentina','r')
                for item in bd_argen.readlines():
                    # name guardara el valor que hay en item 
                    name= item
                    # actualiza el valor de item solo que no toma el salto de linea  
                    name = name[:len(name)-1]
                    # archivo es la direccion de los ids de los genes de una especie 
                    archivo= 'Argentina'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        # bd_argen2 guardara los ids de los genes de una especie 
                        bd_argen2= open(archivo,'r')
                        for item2 in bd_argen2:
                            # se agrega uno por uno de los ids a la lista 
                            self.store_ids.append ([item2])
               
            elif (pais1 =="Australia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Australia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Australia'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
             
            elif (pais1 =="Brasil"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Brasil','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Brasil'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
            
            elif (pais1 =="China"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_China','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'China'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Colombia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Colombia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Colombia'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Filipinas"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Filipinas','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Filipinas'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="India"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_India','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'India'+'/'+name+ '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Indonesia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Indonesia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Indonesia'+'/'+name +'_/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Jamaica"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Jamaica','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Jamaica'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
            
            elif (pais1 =="Madagascar"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Madagascar','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Madagascar'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Srilanka"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Srilanka','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Srilanka'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])

            elif (pais1 =="Tailandia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Tailandia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Tailandia'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie1 == item):                     
                        self.store_ids.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids.append ([item2])
     
    # Se muestran las especies de un pais, para la segunda secuencia 
    def on_changed_pais_seq2(self,widget):
        text_pais_seq2 = widget.get_active_text()
        print(text_pais_seq2)
        if (text_pais_seq2 == "Argentina"):
            self.selec_especie_seq2.get_model().clear()
            bd_argen= open('Paises_selec/fauna_endemica_Argentina','r')
            for item in bd_argen.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Australia"):
            self.selec_especie_seq2.get_model().clear()
            bd_austr= open('Paises_selec/fauna_endemica_Australia','r')
            for item in bd_austr.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Brasil"): 
            self.selec_especie_seq2.get_model().clear()
            bd_brasil= open('Paises_selec/fauna_endemica_Brasil','r')
            for item in bd_brasil.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "China"):
            self.selec_especie_seq2.get_model().clear()
            bd_chi= open('Paises_selec/fauna_endemica_China','r')
            for item in bd_chi.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Colombia"): 
            self.selec_especie_seq2.get_model().clear()
            bd_colo= open('Paises_selec/fauna_endemica_Colombia','r')
            for item in bd_colo.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Filipinas"):
            self.selec_especie_seq2.get_model().clear()
            bd_fili= open('Paises_selec/fauna_endemica_Filipinas','r')
            for item in bd_fili.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "India"): 
            self.selec_especie_seq2.get_model().clear()
            bd_indi= open('Paises_selec/fauna_endemica_India','r')
            for item in bd_indi.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Indonesia"):
            self.selec_especie_seq2.get_model().clear()
            bd_indo= open('Paises_selec/fauna_endemica_Indonesia','r')
            for item in bd_indo.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Jamaica"): 
            self.selec_especie_seq2.get_model().clear()
            bd_jama= open('Paises_selec/fauna_endemica_Jamaica','r')
            for item in bd_jama.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Madagascar"):
            self.selec_especie_seq2.get_model().clear()
            bd_mada= open('Paises_selec/fauna_endemica_Madagascar','r')
            for item in bd_mada.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Srilanka"):
            self.selec_especie_seq2.get_model().clear()
            bd_sri= open('Paises_selec/fauna_endemica_Srilanka','r')
            for item in bd_sri.readlines():
                self.selec_especie_seq2.append_text(item)
        elif (text_pais_seq2 == "Tailandia"): 
            self.selec_especie_seq2.get_model().clear()
            bd_tai= open('Paises_selec/fauna_endemica_Tailandia','r')
            for item in bd_tai.readlines():
                self.selec_especie_seq2.append_text(item)        
        
    # Se muestra los ids de la especie escogida, para la segunda secuencia  
    def on_changed_especie_seq2(self,widget):
        # tipo 1 sera el valor seleccionado del tipo ya sea gen o proteina 
        tipo1 = self.tipo_combobox.get_active_text()
        # pais1 sera el pais escogido 
        pais2 = self.selec_pais_seq2.get_active_text()
        # especie1 sera la especie escogida con respecto a su pais  
        especie2 = self.selec_especie_seq2.get_active_text()
        if tipo1 == "Gen":
            if (pais2 =="Argentina"):
                # bd_argen, guarda la lista de las especies de Argentina 
                bd_argen= open('Paises_selec/fauna_endemica_Argentina','r')
                for item in bd_argen.readlines():
                    # name guardara el valor que hay en item 
                    name= item
                    # actualiza el valor de item solo que no toma el salto de linea  
                    name = name[:len(name)-1]
                    # archivo es la direccion de los ids de los genes de una especie 
                    archivo= 'Argentina'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        # bd_argen2 guardara los ids de los genes de una especie 
                        bd_argen2= open(archivo,'r')
                        for item2 in bd_argen2:
                            # se agrega uno por uno de los ids a la lista 
                            self.store_ids_seq2.append ([item2])
               
            elif (pais2 =="Australia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Australia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Australia'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])
             
            elif (pais2 =="Brasil"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Brasil','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Brasil'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])
            
            elif (pais2 =="China"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_China','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'China'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])

            elif (pais2 =="Colombia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Colombia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Colombia'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])

            elif (pais2 =="Filipinas"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Filipinas','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Filipinas'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])

            elif (pais2 =="India"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_India','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'India'+'/'+name+ '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])

            elif (pais2 =="Indonesia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Indonesia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Indonesia'+'/'+name +'_/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])

            elif (pais2 =="Jamaica"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Jamaica','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Jamaica'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])
            
            elif (pais2 =="Madagascar"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Madagascar','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Madagascar'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])

            elif (pais2 =="Srilanka"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Srilanka','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Srilanka'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])

            elif (pais2 =="Tailandia"):
                # archivo= '/home/alexandra/Escritorio/Argentina/'+ item
                bd_aus= open('Paises_selec/fauna_endemica_Tailandia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Tailandia'+'/'+name + '/'+ name+'_GENES'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])
        elif tipo1 == "Proteína":
            if (pais2 =="Argentina"):
                bd_argen= open('Paises_selec/fauna_endemica_Argentina','r')
                for item in bd_argen.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Argentina'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_argen2= open(archivo,'r')
                        for item2 in bd_argen2:
                            self.store_ids_seq2.append ([item2])
               
            elif (pais2 =="Australia"):
                bd_aus= open('Paises_selec/fauna_endemica_Australia','r')
                for item in bd_aus.readlines():
                    name= item
                    name = name[:len(name)-1]
                    archivo= 'Australia'+'/'+name + '/'+ name+'_PROTEINAS'
                    if( especie2 == item):                     
                        self.store_ids_seq2.clear()
                        bd_aus2= open(archivo,'r')
                        for item2 in bd_aus2:
                            self.store_ids_seq2.append ([item2])


    def on_activated_seq1(self, widget, row, col):
        model = widget.get_model()
        current_id1 = model[row][0]
        #numId=current_id
        #open_fasta= WinFasta()
        print(current_id1)
        '''
        if current_id == "----------------------":
            self.store_ids.clear()
            self.store_ids.append (["A.123"])
            self.store_ids.append (["A.15615"])
            self.store_ids.append (["A.515"])
            self.store_ids.append (["A.4555"])
            self.store_ids.append (["A.515415"])
        '''
    def on_activated_seq2(self, widget, row, col):
        model = widget.get_model()
        current_id2 = model[row][0]
        # numId=current_id
        print(current_id2)       
    


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
        
        # haciendo la ventana scrolable
        self.scrolled_window_main = gtk.ScrolledWindow()

        #########################################
        #     Eleccion del tipo de secuencia    #
        #########################################
        self.tipo_seq_label = gtk.Label()
        self.tipo_seq_label.set_markup("<b>Selecciona un tipo de secuencia:</b>")

        # ComoboxTex para elegir el tipo de secuencia
        self.selec_tipo_seq = gtk.combo_box_new_text()
        #self.selec_gen.connect("changed",self.on_changed_selec_gen)
        # Items del combobox (especies disponibles, inicialmente vacio)
        self.selec_tipo_seq.append_text("Gen")
        self.selec_tipo_seq.append_text("Proteína")

        ##################################
        #             Listas             #
        ##################################
        ########## Mensajes para la secuencias 
        # mensaje de seleccion de la secuencia
        self.mensaje_seleccion_seq = []
        # mensaje de selecion del pais
        self.seleccion_pais_label = []
        # mensaje de seleccion de la especie
        self.seleccion_especie_label = []
        # mensaje de seleccion de ids
        self.seleccion_ids_label = []

        self.seleccion_pais = []
        self.seleccion_especie = []
        self.treeview = []
        self.store_ids = []
        self.column = []
        self.scrolled_window = []


        for i in range(2):
            # mensaje de seleccion de la secuencia
            self.mensaje_seleccion_seq.append(gtk.Label())
            self.mensaje_seleccion_seq[i].set_markup("<b>Selecciona la secuencia #"+str(i+1)+":</b>")

            ########## PAISES
            # mensaje de selecion del pais
            self.seleccion_pais_label.append(gtk.Label("País:"))
            # ComoboxTex para elegir el pais
            self.seleccion_pais.append(gtk.combo_box_new_text())
            #self.seleccion_pais.append[i].connect("changed",self.on_changed_pais)
            # Items del combobox (paises disponibles)
            self.seleccion_pais[i].append_text("Argentina")
            self.seleccion_pais[i].append_text("Australia")
            self.seleccion_pais[i].append_text("Brasil")

            ########## ESPECIES
            # mensaje de seleccion de la especie
            self.seleccion_especie_label.append(gtk.Label("Especie:"))
            # ComoboxTex para elegir la especie
            self.seleccion_especie.append(gtk.combo_box_new_text())
            #self.seleccion_especie[i].connect("changed",self.on_changed_especie)
            # Items del combobox (especies disponibles, inicialmente vacio)
            self.seleccion_especie[i].append_text("------")

            ########## TREEVIEW PARA LOS IDS
            # mensaje de seleccion de ids
            self.seleccion_ids_label.append(gtk.Label("Selecciona un id haciendo doble click sobre él:"))
            # treeView para elegir el ID
            self.treeview.append(gtk.TreeView())
            #self.treeview[i].connect("row-activated", self.on_activated)

            ########## STORE DE LOS IDS
            # Items de los IDs (IDs disponibles, inicialmente vacio)
            self.store_ids.append(gtk.ListStore(str))
            self.store_ids[i].append(["----------------------"])
            self.treeview[i].set_model(self.store_ids[i])

            ########## COLUMNA DEL TREEVIEW
            #self.rendererText = gtk.CellRendererText()
            self.column.append(gtk.TreeViewColumn("Secuencias\nDisponibles", gtk.CellRendererText(), text=0))
            # Agregando la columna al treeView
            self.treeview[i].append_column(self.column[i])
            self.treeview[i].set_headers_visible(False)
            self.treeview[i].set_enable_search(True)

            ########## SCROLLED WINDOW
            self.scrolled_window.append(gtk.ScrolledWindow())
            self.scrolled_window[i].add(self.treeview[i])

        #############################
        #  Align: tipo y parametros #
        #############################
        # boton para agregar otra secuencia
        self.agregar_button = gtk.Button("Agregar una secuencia")
        self.agregar_button.connect("clicked",self.alignM_Button)

        # mensaje para seleccionar el tipo de alineamiento
        self.mensaje_aling_type = gtk.Label()
        self.mensaje_aling_type.set_markup("<b>Selecciona el tipo de alineamiento:</b>")

        self.combobox_align_type = gtk.combo_box_new_text()
        self.combobox_align_type.append_text("Local")
        self.combobox_align_type.append_text("Global")

        # boton para alinear
        self.mensaje_align_butoon = gtk.Label()
        self.mensaje_align_butoon.set_markup("<b>Presiona para alinear:</b>")
        self.align_button = gtk.Button("Alinear")

        ###########################
        #    Boxes Individuales   #
        ###########################
        # mensaje de seleccion del tipo de secuencia
        self.hbox_seleccion_tipo_seq = gtk.HBox()
        self.hbox_seleccion_tipo_seq.pack_start(self.tipo_seq_label,expand=False, fill=False, padding = 30)
        self.hbox_seleccion_tipo_seq.pack_start(self.selec_tipo_seq,expand=False, fill=False)
        
        # inicializamos las listas
        self.hbox_mensaje_seleccion_seq = []
        
        self.label_pais = []
        self.label_especie = []
        self.label_pais_especie = []
        
        self.mensaje_seleccion_ids = []
        self.lista_ids = []

        for i in range(2):
            # mensaje de seleccion de secuencias 
            self.hbox_mensaje_seleccion_seq.append(gtk.HBox())
            self.hbox_mensaje_seleccion_seq[i].pack_start(self.mensaje_seleccion_seq[i],expand=False, fill=False, padding = 30)
            
            # seleccion de pais: label y combobox
            self.label_pais.append(gtk.HBox())
            self.label_pais[i].pack_start(self.seleccion_pais_label[i],expand=False, fill=False, padding = 30)
            self.label_pais[i].pack_start(self.seleccion_pais[i])
            # seleccion de especie: label y combobox
            self.label_especie.append(gtk.HBox())
            self.label_especie[i].pack_start(self.seleccion_especie_label[i],expand=False, fill=False, padding = 30)
            self.label_especie[i].pack_start(self.seleccion_especie[i])
            # union de la seleccion de pais y especie
            self.label_pais_especie.append(gtk.HBox())
            self.label_pais_especie[i].pack_start(self.label_pais[i],expand=False, fill=False)
            self.label_pais_especie[i].pack_start(self.label_especie[i],expand=False, fill=False,padding = 40)

            # mensaje de seleccion de id
            self.mensaje_seleccion_ids.append(gtk.HBox())
            self.mensaje_seleccion_ids[i].pack_start(self.seleccion_ids_label[i],expand=False, fill=False, padding = 30)

            # lista de ids disponibles
            self.lista_ids.append(gtk.HBox())
            self.lista_ids[i].pack_start(self.scrolled_window[i],padding = 30)

        # boton para agregar otra secuencia
        self.hbox_boton_agregar_seq =  gtk.HBox()
        self.hbox_boton_agregar_seq.pack_start(self.agregar_button,expand=False, fill=False,padding = 30)     

        # seleccion tipo de alineamiento
        self.box_seleccion_tipo_aling = gtk.HBox()
        self.box_seleccion_tipo_aling.pack_start(self.mensaje_aling_type,expand=False, fill=False, padding = 30)
        self.box_seleccion_tipo_aling.pack_start(self.combobox_align_type,expand=False, fill=False)

        # boton de alineamiento
        self.hbox_boton_aling =  gtk.HBox()
        self.hbox_boton_aling.pack_start(self.mensaje_align_butoon,expand=False, fill=False, padding = 30)
        self.hbox_boton_aling.pack_start(self.align_button,expand=False, fill=False)

        ########################
        #     Box Principal    #
        ########################
        self.box_main_alignM = gtk.VBox(homogeneous =True)

        self.box_main_alignM.pack_start(self.hbox_seleccion_tipo_seq,expand=False, fill=False, padding = 30)
        
        for i in range(2):
            self.box_main_alignM.pack_start(self.hbox_mensaje_seleccion_seq[i],expand=False, fill=False)
            self.box_main_alignM.pack_start(self.label_pais_especie[i],expand=False, fill=False, padding = 10)
            self.box_main_alignM.pack_start(self.mensaje_seleccion_ids[i],expand=False, fill=False)
            self.box_main_alignM.pack_start(self.lista_ids[i], padding = 10)
        
        self.count_seqs = 2

        self.box_main_alignM.pack_start(self.hbox_boton_agregar_seq,expand=False, fill=False, padding = 10)
        self.box_main_alignM.pack_start(self.box_seleccion_tipo_aling,expand=False, fill=False, padding = 20)
        self.box_main_alignM.pack_start(self.hbox_boton_aling,expand=False, fill=False,padding=10)
        
        self.scrolled_window_main.add_with_viewport(self.box_main_alignM)
        self.add(self.scrolled_window_main)

        self.show_all()


    def on_destroy(self,widget):
        widget.hide()

    def alignM_Button(self,win):
        print("boton!!!")
        self.box_main_alignM.remove(self.hbox_boton_agregar_seq)
        self.box_main_alignM.remove(self.box_seleccion_tipo_aling)
        self.box_main_alignM.remove(self.hbox_boton_aling)

        ##################################
        #    Creando nueva secuencia     #
        ##################################
        self.count_seqs = self.count_seqs+1
        # mensaje de seleccion de la secuencia
        self.mensaje_seleccion_seq.append(gtk.Label())
        self.mensaje_seleccion_seq[self.count_seqs-1].set_markup("<b>Selecciona la secuencia #"+str(self.count_seqs)+":</b>")

        ########## PAISES#
        # mensaje de selecion del pais
        self.seleccion_pais_label.append(gtk.Label("País:"))
        # ComoboxTex para elegir el pais
        self.seleccion_pais.append(gtk.combo_box_new_text())
        #self.seleccion_pais.append[self.count_seqs-1].connect("changed",self.on_changed_pais)
        # Items del combobox (paises disponibles)
        self.seleccion_pais[self.count_seqs-1].append_text("Argentina")
        self.seleccion_pais[self.count_seqs-1].append_text("Australia")
        self.seleccion_pais[self.count_seqs-1].append_text("Brasil")

        ########## ESPECIES
        # mensaje de seleccion de la especie
        self.seleccion_especie_label.append(gtk.Label("Especie:"))
        # ComoboxTex para elegir la especie
        self.seleccion_especie.append(gtk.combo_box_new_text())
        #self.seleccion_especie[self.count_seqs-1].connect("changed",self.on_changed_especie)
        # Items del combobox (especies disponibles, inicialmente vacio)
        self.seleccion_especie[self.count_seqs-1].append_text("------")

        ########## TREEVIEW PARA LOS IDS
        # mensaje de seleccion de ids
        self.seleccion_ids_label.append(gtk.Label("Selecciona un id haciendo doble click sobre él:"))
        # treeView para elegir el ID
        self.treeview.append(gtk.TreeView())
        #self.treeview[self.count_seqs-1].connect("row-activated", self.on_activated)

        ########## STORE DE LOS IDS
        # Items de los IDs (IDs disponibles, inicialmente vacio)
        self.store_ids.append(gtk.ListStore(str))
        self.store_ids[self.count_seqs-1].append(["----------------------"])
        self.treeview[self.count_seqs-1].set_model(self.store_ids[self.count_seqs-1])

        ########## COLUMNA DEL TREEVIEW
        #self.rendererText = gtk.CellRendererText()
        self.column.append(gtk.TreeViewColumn("Secuencias\nDisponibles", gtk.CellRendererText(), text=0))
        # Agregando la columna al treeView
        self.treeview[self.count_seqs-1].append_column(self.column[self.count_seqs-1])
        self.treeview[self.count_seqs-1].set_headers_visible(False)
        self.treeview[self.count_seqs-1].set_enable_search(True)

        ########## SCROLLED WINDOW
        self.scrolled_window.append(gtk.ScrolledWindow())
        self.scrolled_window[self.count_seqs-1].add(self.treeview[self.count_seqs-1])

        ###########################
        #    Boxes Individuales   #
        ###########################
        # mensaje de seleccion de secuencias 
        self.hbox_mensaje_seleccion_seq.append(gtk.HBox())
        self.hbox_mensaje_seleccion_seq[self.count_seqs-1].pack_start(self.mensaje_seleccion_seq[self.count_seqs-1],expand=False, fill=False, padding = 30)

        # seleccion de pais: label y combobox
        self.label_pais.append(gtk.HBox())
        self.label_pais[self.count_seqs-1].pack_start(self.seleccion_pais_label[self.count_seqs-1],expand=False, fill=False, padding = 30)
        self.label_pais[self.count_seqs-1].pack_start(self.seleccion_pais[self.count_seqs-1])
        # seleccion de especie: label y combobox
        self.label_especie.append(gtk.HBox())
        self.label_especie[self.count_seqs-1].pack_start(self.seleccion_especie_label[self.count_seqs-1],expand=False, fill=False, padding = 30)
        self.label_especie[self.count_seqs-1].pack_start(self.seleccion_especie[self.count_seqs-1])
        # union de la seleccion de pais y especie
        self.label_pais_especie.append(gtk.HBox())
        self.label_pais_especie[self.count_seqs-1].pack_start(self.label_pais[self.count_seqs-1],expand=False, fill=False)
        self.label_pais_especie[self.count_seqs-1].pack_start(self.label_especie[self.count_seqs-1],expand=False, fill=False,padding = 40)

        # mensaje de seleccion de id
        self.mensaje_seleccion_ids.append(gtk.HBox())
        self.mensaje_seleccion_ids[self.count_seqs-1].pack_start(self.seleccion_ids_label[self.count_seqs-1],expand=False, fill=False, padding = 30)

        # lista de ids disponibles
        self.lista_ids.append(gtk.HBox())
        self.lista_ids[self.count_seqs-1].pack_start(self.scrolled_window[self.count_seqs-1], padding = 30)

        ########################
        #     Box Principal    #
        ########################
        self.box_main_alignM.pack_start(self.hbox_mensaje_seleccion_seq[self.count_seqs-1],expand=False, fill=False)
        self.box_main_alignM.pack_start(self.label_pais_especie[self.count_seqs-1],expand=False, fill=False, padding = 10)
        self.box_main_alignM.pack_start(self.mensaje_seleccion_ids[self.count_seqs-1],expand=False, fill=False)
        self.box_main_alignM.pack_start(self.lista_ids[self.count_seqs-1], padding = 10)

        self.box_main_alignM.pack_start(self.hbox_boton_agregar_seq,expand=False, fill=False, padding = 10)
        self.box_main_alignM.pack_start(self.box_seleccion_tipo_aling,expand=False, fill=False, padding = 20)
        self.box_main_alignM.pack_start(self.hbox_boton_aling,expand=False, fill=False,padding=10)

        self.show_all()


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


        ############################
        #     Eleccion del gen     #
        ############################
        name_gene = gtk.Label()
        name_gene.set_markup("<b>Selecciona un gen:</b>")
        
        # ComoboxTex para elegir el gen
        self.selec_gen = gtk.combo_box_new_text()
        #self.selec_gen.connect("changed",self.on_changed_selec_gen)
        # Items del combobox (especies disponibles, inicialmente vacio)
        self.selec_gen.append_text("------")        
        

        ##################################################
        #   TreeView para seleccionar uno o mas paises   #
        ##################################################   
        # treeView para elegir los paises
        treeView_gene = gtk.TreeView()
        #treeView_gene.connect("row-activated", self.on_activated_gene)

        # Items de los IDs (IDs disponibles, inicialmente vacio)
        self.store_gene = gtk.ListStore(str,bool)
        self.store_gene.append(["----------------------",False])
        treeView_gene.set_model(self.store_gene)
        treeView_gene.set_enable_search(True)

        # Columna 1
        rendererText_gene = gtk.CellRendererText()
        column_gene = gtk.TreeViewColumn("Países\nDisponibles", rendererText_gene, text=0) 
        # Agregando la columna al treeView
        treeView_gene.append_column(column_gene)

        # Columna 2
        rendererText_gene2 = gtk.CellRendererToggle()
        rendererText_gene2.set_property('activatable',True)
        rendererText_gene2.connect('toggled', self.cell_toggled,self.store_gene)
        column_gene2 = gtk.TreeViewColumn("Selecciona", rendererText_gene2,active=1)
        # Agregando la columna al treeView
        treeView_gene.append_column(column_gene2)

        # ScrolledWindow
        scrolled_window_gene = gtk.ScrolledWindow()
        scrolled_window_gene.add(treeView_gene)


        ###################################
        #   Boton para generar el arbol   #
        ###################################
        self.generar_arbol = gtk.Button("Generar Árbol")
        self.generar_arbol.connect("clicked",self.ver_arbol)


        ########################
        #   Boxes terciarios   #
        ########################
        # HBox para el mensaje de seleccion del gen
        box_mensaje_gen = gtk.HBox()
        box_mensaje_gen.pack_start(name_gene,expand=False, fill=False,padding = 30)
        box_mensaje_gen.pack_start(self.selec_gen,expand=False, fill=False)

        # Hbox para la lista de genes
        box_gene_list = gtk.HBox()
        box_gene_list.pack_start(scrolled_window_gene, padding =30)

        #HBox para mostrar boton para mostrar arbol
        box_ver_arbol = gtk.HBox()
        box_ver_arbol.pack_start(self.generar_arbol,expand=False, fill=False, padding = 30)

        # HBox para mostrar el arbol generado
        self.box_tree_show = gtk.HBox()
        self.arbol = 0

        #########################
        #   Boxes secundarios   #
        #########################
        # VBox para el mensaje y combobox para seleccionar el gen
        box_parte1_gene = gtk.VBox()
        box_parte1_gene.pack_start(box_mensaje_gen,expand=False, fill=False, padding = 20)

        # VBox para ver el treeView
        box_parte2_gene = gtk.VBox()
        box_parte2_gene.pack_start(box_gene_list)        

        # VBox para el boton de generar arbol
        box_parte3_gene = gtk.VBox()
        box_parte3_gene.pack_start(box_ver_arbol,expand=False, fill=False,padding=10)
        box_parte3_gene.pack_start(self.box_tree_show,expand=False, fill=False,padding=10)


        ########################
        #     Box Principal    #
        ########################
        box_main_gene = gtk.VBox()
        box_main_gene.pack_start(box_parte1_gene, expand=False, fill=False)
        box_main_gene.pack_start(box_parte2_gene)
        box_main_gene.pack_start(box_parte3_gene, expand=False, fill=False)

        self.add(box_main_gene)
        self.show_all()
        
    def on_destroy(self,widget):
        widget.hide()

    def cell_toggled(self,cell,path,model):
        model[path][1] = not model[path][1]
        print("toogle '%s' to: %s" % (model[path][0], model[path][1]),)
        
    def ver_arbol(self,win):
        print("Mostrar arbol!!!")
        if self.arbol == 0:
            # Imagen del arbol   
            self.tree_image = gtk.Image()
            self.tree_image.set_from_file("treesample.png")
            self.box_tree_show.pack_start(self.tree_image,expand=False, fill=False, padding = 30)
            self.arbol = 1
            self.show_all()


class PyApp(gtk.Window):
    def __init__(self):
        # creando la ventana
        super(PyApp,self).__init__()
        self.set_default_size(320,330)
        self.set_title("My Biology App")
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_resizable(False)

        ########## Primer boton
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
        

        ########## Segundo boton
        alignM = gtk.Button("Alineamiento Múltiple")
        
        #crear a gdk.color para el color del boton  
        map = alignM.get_colormap() 
        color = map.alloc_color("#9F81F7") 
        
        #copiar el estilo actual y reemplazarlo 
        style = alignM.get_style().copy()
        style.bg[gtk.STATE_NORMAL] = color 
        
        #cambiar el estilo del boton por el estilo escogido  
        alignM.set_style(style)  
 
        alignM.connect("clicked",self.alignM_Event)
        alignM.set_size_request(200,40)


        ########## Tercer Boton
        tree = gtk.Button("Árbol Filogenético")
        
        #crear a gdk.color para el color del boton  
        map = tree.get_colormap() 
        color = map.alloc_color("#FA8258") 
        
        #copiar el estilo actual y reemplazarlo 
        style = tree.get_style().copy()
        style.bg[gtk.STATE_NORMAL] = color 
        
        #cambiar el estilo del boton por el estilo escogido  
        tree.set_style(style)  
        
        tree.connect("clicked",self.tree_Event)
        tree.set_size_request(200,40)
        
        ########## Boton de About
        about = gtk.Button("Acerca de")
        about.connect("clicked",self.showAbout)
        about.set_size_request(85,25)

        ########## Mensaje de Bienvenida
        message = gtk.Label()
        message.set_markup("<b><big>¡Bienvenido a My Biology App!</big></b>")
        
        ########## Mensaje que pide seleccionar una opcion
        message2= gtk.Label()
        message2.set_markup("<b>Selecciona una opción:</b>")
        
        # HBox del mensaje de bienvenida
        box_message = gtk.HBox()
        box_message.pack_start(message,expand=False, fill=False,padding=20)

        # HBox del mensaje para seleccionar una opcion
        box_message2 = gtk.HBox()
        box_message2.pack_start(message2,expand=False, fill=False,padding=20)
        
        # HBox para el primer boton
        box_align = gtk.HBox()
        box_align.pack_start(align,padding = 70)

        # HBox para el segundo boton
        box_alignM = gtk.HBox()
        box_alignM.pack_start(alignM,padding = 70)

        # HBox para el tercer boton
        box_tree = gtk.HBox()
        box_tree.pack_start(tree,padding = 70)

        # HBox para el boton de about
        box_about = gtk.HBox()
        box_about.pack_start(about,expand=False, fill=False,padding=20)

        box_main = gtk.VBox()
        box_main.pack_start(box_message,padding = 20)
        box_main.pack_start(box_message2,padding = 20)
        box_main.pack_start(box_align)
        box_main.pack_start(box_alignM)
        box_main.pack_start(box_tree)
        box_main.pack_start(box_about, padding = 20)

        self.add(box_main)

    def align_Event(self,win):
        print("Alineamiento Simple!!")
        align_Win = anotherWinAlign()
        
    def alignM_Event(self,win):
        print("Alineamiento Múltiple!!")
        alignM_Win = anotherWinAlignM()

    
    def tree_Event(self,win):
        print("Árbol Filogenético!!")
        tree_Win = anotherWinTree()


    def showAbout(self,win):
        about = gtk.AboutDialog()
        about.set_program_name("My Biology App")
        about.set_authors(["Chia", "Ale", "Melissa", "Hazard"])
        about.set_copyright("(c) computer science students")
        about.set_comments("Course: Biología Computacional")
        about.run()
        about.destroy()

window = PyApp()
window.connect("destroy",gtk.main_quit)
window.show_all()
gtk.main()
