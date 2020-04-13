object Laboratorio10L {
  def main(args: Array[String]) = {
    print("Ingrese el numero a evaluar: ")
    val n = scala.io.StdIn.readInt()
    var cont = 0
    for (i <- 1 to n-1) {
      if (n%i==0) {
        cont += i
      }
     }
    if (cont==n) {
      println("El numero es perfecto")
    } else {
      println("El numero no es perfecto")
    }
  }
}
