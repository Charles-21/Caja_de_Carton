program fibonacci

	implicit none
	integer :: i,n
	integer, allocatable :: fib(:)
	character(len=30) :: nombre_archivo
	integer :: archivo

	! Archivo de salida:

	nombre_archivo = "fibonacci.txt"


	!Saludar... ya!

	print *, "Hello, Fibonacci!"

	!Cuántos términos?

	print *, "¿Cuántos términos de la sucesión de Fibonacci quieres ver, hdlv?"
	read *, n

	! n debe ser mayor que 0

	if (n<=0) then
		print *, "Debes ingresar un número mayor a 0, hdlv!"
		stop
	end if


	! Reservamos espacio para los n términos
	allocate(fib(n))

	! Calcula la sucesión

	fib(1) = 0

	if  (n>=2) fib(2) = 1

	do i=3, n
		fib(i) = fib(i-1) + fib(i-2)
	end do

	! Imprimimos la sucesión

	print *, "Sucesion de Fibonacci:"

	do i=1, n
		print *, fib(i)
	end do

	! Guardar como: Indice valor

	open(unit=10, file=nombre_archivo, status='replace')

	do i=1, n
		write(10,*) i, fib(i)
	end do

	close(10)

	print*, "Los resultados han sido guardados en ", trim(nombre_archivo)


	! Liberamos memoria
	deallocate(fib)

end program


