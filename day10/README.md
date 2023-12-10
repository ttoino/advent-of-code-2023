# Day 10: Pipe Maze

You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "[Hot Springs](https://en.wikipedia.org/wiki/Hot_spring)" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of **tiles**:

- `|` is a **vertical pipe** connecting north and south.
- `-` is a **horizontal pipe** connecting east and west.
- `L` is a **90-degree bend** connecting north and east.
- `J` is a **90-degree bend** connecting north and west.
- `7` is a **90-degree bend** connecting south and west.
- `F` is a **90-degree bend** connecting south and east.
- `.` is **ground**; there is no pipe in this tile.
- `S` is the **starting position** of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is **one large, continuous loop**.

For example, here is a square loop of pipe:

```
.....
.F-7.
.|.|.
.L-J.
.....
```

If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

<pre><code>.....
.<strong>S</strong>-7.
.|.|.
.L-J.
.....
</code></pre>

In the above diagram, the `S` tile is still a 90-degree `F` bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that **aren't connected to the loop**! This sketch shows the same loop as above:

```
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
```

In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to `S`, pipes those pipes connect to, pipes **those** pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including `S`, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

```
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
```

Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

```
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
```

If you want to **get out ahead of the animal**, you should find the tile in the loop that is **farthest** from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps **along the loop** to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:

```
.....
.S-7.
.|.|.
.L-J.
.....
```

You can count the distance each tile in the loop is from the starting point like this:

<pre><code>.....
.012.
.1.3.
.23<strong>4</strong>.
.....
</code></pre>

In this example, the farthest point from the start is **`4`** steps away.

Here's the more complex loop again:

```
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
```

Here are the distances for each tile on that loop:

<pre><code>..45.
.236.
01.7<strong>8</strong>
14567
23...
</code></pre>

Find the single giant loop starting at `S`. **How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?**

## Part Two

You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is **within the area enclosed by the loop**?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

```
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
```

The above loop encloses merely **four tiles** - the two pairs of `.` in the southwest and southeast (marked `I` below). The middle `.` tiles (marked `O` below) are **not** in the loop. Here is the same loop again with those regions marked:

<pre><code>...........
.S-------7.
.|F-----7|.
.||<strong>OOOOO</strong>||.
.||<strong>OOOOO</strong>||.
.|L-7<strong>O</strong>F-J|.
.|<strong>II</strong>|<strong>O</strong>|<strong>II</strong>|.
.L--J<strong>O</strong>L--J.
.....<strong>O</strong>.....
</code></pre>

In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, `I` is still within the loop and `O` is still outside the loop:

<pre><code>..........
.S------7.
.|F----7|.
.||<strong>OOOO</strong>||.
.||<strong>OOOO</strong>||.
.|L-7F-J|.
.|<strong>II</strong>||<strong>II</strong>|.
.L--JL--J.
..........
</code></pre>

In both of the above examples, **`4`** tiles are enclosed by the loop.

Here's a larger example:

```
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
```

The above sketch has many random bits of ground, some of which are in the loop (`I`) and some of which are outside it (`O`):

<pre><code><strong>O</strong>F----7F7F7F7F-7<strong>OOOO</strong>
<strong>O</strong>|F--7||||||||FJ<strong>OOOO</strong>
<strong>O</strong>||<strong>O</strong>FJ||||||||L7<strong>OOOO</strong>
FJL7L7LJLJ||LJ<strong>I</strong>L-7<strong>OO</strong>
L--J<strong>O</strong>L7<strong>III</strong>LJS7F-7L7<strong>O</strong>
<strong>OOOO</strong>F-J<strong>II</strong>F7FJ|L7L7L7
<strong>OOOO</strong>L7<strong>I</strong>F7||L7|<strong>I</strong>L7L7|
<strong>OOOOO</strong>|FJLJ|FJ|F7|<strong>O</strong>LJ
<strong>OOOO</strong>FJL-7<strong>O</strong>||<strong>O</strong>||||<strong>OOO</strong>
<strong>OOOO</strong>L---J<strong>O</strong>LJ<strong>O</strong>LJLJ<strong>OOO</strong>
</code></pre>

In this larger example, **`8`** tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

```
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
```

Here are just the tiles that are **enclosed by the loop** marked with `I`:

<pre><code>FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ<strong>I</strong>F7FJ-
L---JF-JLJ<strong>IIII</strong>FJLJJ7
|F|F-JF---7<strong>III</strong>L7L|7|
|FFJF7L7F-JF7<strong>II</strong>L---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
</code></pre>

In this last example, **`10`** tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop. **How many tiles are enclosed by the loop?**
