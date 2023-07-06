import JahirPineda_PGY1121_007_D as fn

while True:
    fn.ver_menu()
    opcion = fn.validar_opcion()
    if opcion==1:
        fn.comprar_entradas()
        fn.validar_tipo_entrada()
        fn.validar_rut()
        fn.ver_ubicaciones()
    elif opcion==2:
        fn.ver_ubicaciones()
    elif opcion==3:
        fn.ver_asistentes()
    elif opcion==4:
        fn.mostrar_ganancias()
    elif opcion==5:
        fn.mensaje_despedida()
        break
