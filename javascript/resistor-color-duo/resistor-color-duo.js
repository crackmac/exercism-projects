//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const COLORS = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white'
]

export const decodedValue = (colors) => {
  return((COLORS.indexOf(colors[0]) * 10 )+ COLORS.indexOf(colors[1]))
  // throw new Error("Remove this statement and implement this function");
};
