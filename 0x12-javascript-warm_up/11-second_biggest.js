#!/usr/bin/node
const argv = process.argv;
if (argv.length >= 3) {
  const argc = argv.length;
  let n1 = argv[2];
  for (let index = 2; index < argc; index++) {
    if (Number(n1) < Number(argv[index])) n1 = argv[index];
  }
  console.log(n1);
}
