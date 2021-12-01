import scala.io.Source

val data = Source.fromFile("input.txt").getLines.toArray.map(_.toInt)

val n_increases = (data.dropRight(1) zip data.drop(1))
  .filter(t => t._2 - t._1 > 0)
  .length

println(n_increases)

val lag0 = data.dropRight(2)
val lag1 = data.drop(1).dropRight(1)
val lag2 = data.drop(2)

val data_rolling = (lag0, lag1, lag2).zipped.toList.map(t => t._1 + t._2 + t._3)
val n_increases_rolling = (data_rolling.dropRight(1) zip data_rolling.drop(1))
  .filter(t => t._2 - t._1 > 0)
  .length

println(n_increases_rolling)
