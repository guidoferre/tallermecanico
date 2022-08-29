from django.urls import path, include
from blog.views import About, Cliente, ClienteCreate, ClienteDelete, ClienteDetail, ClienteList, EditaElimina, EditarDatos, LoginView, Quienes_Somos, agregar_avatar, cliente, contact, editar_perfil, editarCliente, eliminarCliente, lista_clientes, mecanico, BusquedaCliente, ClienteFormulario, mecanicoFormulario, register, reparacion, inicio, Buscar, listaMecanicos, deleteMecanico, updateMecanico
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('blog/', include('appMensajeria.urls', namespace='appMensajeria')),
    path('inicio/', inicio, name="inicio"),
    path('cliente/', Cliente, name ='cliente'),
    path('quienes_somos/', Quienes_Somos, name ='quienesSomos'),
    path('mecanico/', mecanico, name="mecanico"),
    path('Reparaciones/<int:start_page>', reparacion, name= "reparaciones"),
    path('clienteFormulario/',ClienteFormulario, name="clienteFormulario" ),
    path('mecanicoFormulario/',mecanicoFormulario, name="MecanicoFormulario" ),
    path('buscarcliente/', BusquedaCliente, name="BusquedaCliente" ),
    path('buscar/', Buscar , name ="Buscar" ), 
    path('lista-clientes/', lista_clientes, name ="lista" ), 
    path('eliminacliente/<int:id>', eliminarCliente, name ="eliminaCliente" ), 
    path('editaCliente/<int:id>', editarCliente, name ="editarCliente" ), 
    path('clientelist', ClienteList.as_view(), name ="clientelist" ),
    path('detailcliente/<int:pk>', ClienteDetail.as_view(), name ="clientesDetail" ),  
    path('CreaCliente/', ClienteCreate.as_view(), name ="CreaCliente" ),  
    path('EliminarCliente/<int:pk>', ClienteDelete.as_view(), name ="EliminarCliente" ),  
    path('login/', LoginView, name ="Login" ),  
    path('registro/', register, name ="Registrar" ),  
    path('logout/', LogoutView.as_view(template_name='logout.html'), name ="Logout" ),  
    path('editar-perfil/', editar_perfil, name ="EditarPerfil" ), 
    path('agregar-avatar/', agregar_avatar, name ="CrearAvatar" ),  
    path('editar-datos/', EditarDatos, name ="EditarDatos" ),  
    path('EditaEliminaCliente/', EditaElimina, name ="EditaEliminaCliente" ), 
    path('listaMecanicos/', listaMecanicos, name ="listaMecanicos" ), 
    path('updateMecanico/<int:id>', updateMecanico, name ="updateMecanico" ), 
    path('deleteMecanico/<int:pk>', deleteMecanico.as_view(), name ="deleteMecanico" ),  
    path('about/', About, name ="About" ), 
    path('contact/', contact, name ="contact" ), 


]
