import random


titulo="Historia de los chorros"

print ("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
numero_random= random.randint(1,50)
calculo= 15*numero_random


print ("Te encuentras caminando con tus compañeros tranquilamente por la calle. Todos estan borrachos y "
       "deciden cruzar hacia la ruta.\n"
       "De repente un grupo de 5 chicos los cruza de forma apresurada poniendose en frente de ustedes."
       "Uno de ellos saca una navaja y les dice que le den todas sus pertenencias\n"
       "Una parte del grupo, reunido de valor y coraje, decide enfrentar a estos chicos y otra parte sale corriendo")

opcion = input ("[OPCION A - SALES CORRIENDO TRATANDO DE EVITAR CUALQUIER PROBLEMA / OPCION B - TE QUEDAS "
                "PARA ENFRENTAR A LOS LADRONES CON TUS AMIGOS]\n")
if opcion == "A":
    opcion = input ("Sales corriendo. Mientras la otra parte del grupo entretiene a los ladrones uno de ellos\n"
                    "se percata de que te estas yendo y te persigue. En un punto ves a un coche por las cercanias\n"
                    "¿Que haces?\n"
                    "[OPCION A - NO PARAS AL COCHE / OPCION B - PARAS AL COCHE]\n")
    if opcion == "A":
        print ("No has parado el coche. Los ladrones te han alcanzado con su rapidez! Le han robado todo a ti "
               "y a tus amigos.\n FIN")
        exit ()

    elif opcion == "B":
        opcion = input ("Has parado el coche poniendote enfrente de el. Junto a ti corren 1 chico y 2 chicas.\n"
                        "Le explicas al conductor lo sucedido y este se ofrece a llevarlos a algun lugar seguro\n"
                        "pero sabes que otra parte del grupo se esta peleando con los ladrones y \n"
                        "tal vez necesite ayuda. ¿Que haces?\n [OPCION A - TE SUBES JUNTO A TUS AMIGOS AL COCHE "
                        "Y SE VAN / OPCION B - SUBES A TUS AMIGAS AL AUTO JUNTO A LOS ELEMENTOS DE VALORES Y TE "
                        "QUEDAS A AYUDAR A TUS AMIGOS]\n")
        if opcion == "A":
            print ("Te has subido al auto junto a tus amigos y los has dejado a su propia suerte. \n"
                   "Felicidades! Has salido ileso y con tus elementos de valor, pero eres un \n"
                   "amigo pesimo")
            exit ()
        elif opcion == "B":
            opcion = input ("Tus amigas y tus elementos de valor se han ido a una zona segura.\n"
                            "Vuelves al lugar donde tus amigos se estan peleando y te encuentras\n"
                            "con que uno de ellos esta tirado en el suelo. Los ladrones al ver\n"
                            "que llegas corriendo, se van, llevandose consigo un par de celulares.\n"
                            "[OPCION A - TE QUEDAS PARA ASISTIR A TU AMIGO HERIDO / OPCION B - CORRES TRAS "
                            "LOS LADRONES PARA RECUPERAR LOS CELULARES]\n")
            if opcion == "A":
                print ("Levantas a tu amigo. ¡Esta conciente!. Decides llamar con el movil de tu amigo\n"
                       "(que convenientemente no se lo robaron) al 911 para asistencia.\n FIN")
                exit ()
            elif opcion == "B":
                opcion = input ("Corres tras los ladrones. Llegas a una esquina la cual se divide en 2\n"
                                "calles. Uno de los ladrones se va para la calle izquierda y el otro "
                                "para la derecha.\nSabes que uno de los ladrones tiene los celulares "
                                "pero no sabes quien.\n [OPCION A - CORRES HACIA LA DERECHA/ OPCION B- CORRES"
                                "HACIA LA IZQUIERDA]\n")
                if opcion == "A":
                    print ("Has agarrado al maleante y resulta que no tenia los celulares.\n"
                           "Vuelves al lugar donde estaban tus amigos y resulta que ya no se encuentran alli.\n"
                           "Al no tener tu celular no puedes llamar a ningun taxi. Toca caminar!.\n FIN")
                elif opcion == "B":
                    opcion = int(input ("Has agarrado al maleante y le sacas los celulares. Vuelves a la zona donde\n"
                                    "estaban tus amigos y resulta que ya no se encuentran alli. Utilizas uno de los\n"
                                    "celulares recuperados para llamar al taxi, pero, tiene contraseña. El celular\n"
                                    "muestra que la misma es el resultado de 15 x un numero random que te\n"
                                    "da el celular.\n[ACERTIJO - CALCULA LA CONTRASEÑA]\n. [CUANTO ES 15 x "
                                    "{}]\n".format (numero_random)))
                    if opcion == 15 * numero_random:
                        print ("CORRECTO!. Has decifrado la contraseña. El taxi llega y vas a la zona segura donde\n"
                               "estan todos tus amigos. Al llegar te enteras de que tu amigo herido en realidad\n"
                               "estaba tirado por la borrachera. Felicidades! Nadie salio herido y has recuperado\n"
                               "los celulares.\n Eres el heroe de esta histora!\nFIN")
                        exit()
                    else:
                        print ("INCORRECTO. La contraseña que has introducido es erronea y el celular se te "
                               "acaba de quedar sin bateria. Toca caminar!")
                        exit ()

if opcion == "B":
    opcion = input ("Te quedas. Empiezan a darse de golpes con los ladrones. Consigues dar un golpe certero\n"
                    "y le tiras la navaja al ladron que la tenia. Uno de tus amigos agarra la navaja y la tira\n"
                    "lejos para que nadie la pueda utilizar. En un momento dado la situacion se complica y\n"
                    "derreptente UPA!. Quedas tu solo contra dos ladrones. ¿Que haces?\n [OPCION A - DECIDES "
                    "RENDIRTE Y DARLE TODAS TUS PERTENENCIAS / OPCION B - TE ARMAS DE VALOR Y LOS ENFRENTAS]\n")
    if opcion == "A":
        opcion = input ("Le das tus objetos de valor a los ladrones y se largan. Dos de tus amigos\n"
                        "se encuentran inconcientes y uno de ellos en estado de shock.\n [OPCION A - INTENTAS "
                        "HACER ENTRAR EN RAZON A TU AMIGO SHOCKEADO PARA QUE TE AYUDE / OPCION B - LLAMAS A EMERGENCIAS]\n"
                        "")
        if opcion == "A":
            print ("Intentas hacer entrar en razon a tu amigo dandole una cachetada. Este, al estar en una pelea,\n"
                   "te noquea de 1 golpe. Felicidades! Has sido noqueado por TU propio amigo.\n FIN")
            exit ()

        else:
            opcion = input ("Intentas llamar a emergencias pero de repente aparece una llamada entrante\n"
                            "de uno de los padres de tus amigos.\n[¿LA CONTESTAS? (S/N)] ")
            if opcion == "S":
                opcion = input ("Has contestado la llamada del padre y le has comentado lo que ha sucedido.\n"
                                "Ahora viene en camino al lugar. Cuelgas la llamada y llamas a emergencias")

            elif opcion == "N":
                print ("Has decidido no atender la llamda. Llamas a emergencias rapidamente. Pasan unos\n"
                                "minutos y llega la ambulancia. Te ve el paramedico y se lleva a tus amigos.\n"
                                "Resulta que la ambulancia no queda más lugar por lo que... Toca caminar!"
                                "(debiste haber atendido esa llamada)")
                exit ()
    else:
        print ("Enfrentas a los ladrones. Lamentablemente estas tan borracho que no puedes coordinar muchos más\n"
               "golpes y te terminan tirando al suelo y robandote todas tus pertenencias :(.\n FIN")