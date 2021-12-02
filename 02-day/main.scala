import scala.io.Source

val movesRaw = Source.fromFile("input.txt").getLines.toList

class Submarine {
  var depth = 0
  var position = 0
  var aim = 0

  def processMoveA(move: String) = {
    val direction = move.split(' ')(0)
    val distance = move.split(' ')(1).toInt

    if (direction == "forward") position += distance 
    else if (direction == "down") depth += distance
    else if (direction == "up") depth -= distance
  }

  def processMoveB(move: String) = {
    val direction = move.split(' ')(0)
    val distance = move.split(' ')(1).toInt

    if (direction == "forward") {
      position += distance
      depth += aim*distance
    } else if (direction == "down") {
      aim += distance
    } else if (direction == "up") {
      aim -= distance
    }
  }

}

val sub1 = new Submarine()
for (move <- movesRaw) sub1.processMoveA(move)
println(sub1.position*sub1.depth)

val sub2 = new Submarine()
for (move <- movesRaw) sub2.processMoveB(move)
println(sub2.position*sub2.depth)
