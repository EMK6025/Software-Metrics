
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Calculator implements ActionListener {

    private static JTextField inputBox;

    Calculator() {
    }

    public static void main(String[] args) {
        createWindow();
    }

    private static void createWindow() {
        JFrame frame = new JFrame("Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        createUI(frame);
        frame.setSize(304, 340);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    private static void createUI(JFrame frame) {
        JPanel panel = new JPanel();
        Calculator calculator = new Calculator();
        GridBagLayout layout = new GridBagLayout();
        GridBagConstraints gbc = new GridBagConstraints();
        panel.setLayout(layout);
        inputBox = new JTextField("", 10);
        inputBox.setEditable(false);

        JButton buttonMc = new JButton("mc");
        buttonMc.setBackground(Color.LIGHT_GRAY);
        JButton buttonMr = new JButton("mr");
        buttonMr.setBackground(Color.LIGHT_GRAY);
        JButton buttonMs = new JButton("m-");
        buttonMs.setBackground(Color.LIGHT_GRAY);
        JButton buttonMp = new JButton("m+");
        buttonMp.setBackground(Color.LIGHT_GRAY);

        JButton button1 = new JButton("1");
        button1.setBackground(Color.WHITE);
        JButton button2 = new JButton("2");
        button2.setBackground(Color.WHITE);
        JButton button3 = new JButton("3");
        button3.setBackground(Color.WHITE);
        JButton button4 = new JButton("4");
        button4.setBackground(Color.WHITE);
        JButton button5 = new JButton("5");
        button5.setBackground(Color.WHITE);
        JButton button6 = new JButton("6");
        button6.setBackground(Color.WHITE);
        JButton button7 = new JButton("7");
        button7.setBackground(Color.WHITE);
        JButton button8 = new JButton("8");
        button8.setBackground(Color.WHITE);
        JButton button9 = new JButton("9");
        button9.setBackground(Color.WHITE);
        JButton button0 = new JButton("0");
        button0.setBackground(Color.WHITE);
        JButton buttonDot = new JButton(".");
        buttonDot.setBackground(Color.WHITE);
        JButton buttonToggle = new JButton("+/-");
        buttonToggle.setBackground(Color.WHITE);
        JButton buttonPlus = new JButton("+");
        buttonPlus.setBackground(Color.ORANGE);
        JButton buttonMinus = new JButton("-");
        buttonMinus.setBackground(Color.ORANGE);
        JButton buttonMultiply = new JButton("x");
        buttonMultiply.setBackground(Color.ORANGE);
        JButton buttonDivide = new JButton("/");
        buttonDivide.setBackground(Color.ORANGE);
        JButton buttonClear = new JButton("C");
        buttonClear.setBackground(Color.LIGHT_GRAY);
        JButton buttonSQRT = new JButton("√");
        buttonSQRT.setBackground(Color.LIGHT_GRAY);
        JButton buttonEquals = new JButton("=");
        buttonEquals.setBackground(Color.ORANGE);
        JButton buttonPercent = new JButton("%");
        buttonPercent.setBackground(Color.LIGHT_GRAY);
        JButton buttonPI = new JButton("π");
        buttonPI.setBackground(Color.LIGHT_GRAY);
        JButton buttonExp = new JButton("^");
        buttonExp.setBackground(Color.LIGHT_GRAY);
        JButton buttonR2 = new JButton("R2");
        buttonR2.setBackground(Color.LIGHT_GRAY);
        JButton buttonR0 = new JButton("R0");
        buttonR0.setBackground(Color.LIGHT_GRAY);

        button1.addActionListener(calculator);
        button2.addActionListener(calculator);
        button3.addActionListener(calculator);
        button4.addActionListener(calculator);
        button5.addActionListener(calculator);
        button6.addActionListener(calculator);
        button7.addActionListener(calculator);
        button8.addActionListener(calculator);
        button9.addActionListener(calculator);
        button0.addActionListener(calculator);

        buttonDot.addActionListener(calculator);
        buttonToggle.addActionListener(calculator);
        buttonPlus.addActionListener(calculator);
        buttonMultiply.addActionListener(calculator);
        buttonMinus.addActionListener(calculator);
        buttonDivide.addActionListener(calculator);
        buttonClear.addActionListener(calculator);
        buttonSQRT.addActionListener(calculator);
        buttonEquals.addActionListener(calculator);
        buttonExp.addActionListener(calculator);
        buttonPercent.addActionListener(calculator);
        buttonMc.addActionListener(calculator);
        buttonMr.addActionListener(calculator);
        buttonMs.addActionListener(calculator);
        buttonMp.addActionListener(calculator);
        buttonR2.addActionListener(calculator);
        buttonR0.addActionListener(calculator);
        buttonPI.addActionListener(calculator);

        gbc.fill = GridBagConstraints.BOTH;
        gbc.ipady = 12;
        gbc.ipadx = 20;
        gbc.gridwidth = 4;
        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(inputBox, gbc);
        gbc.gridwidth = 1;
        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(buttonMc, gbc);
        gbc.gridx = 1;
        gbc.gridy = 1;
        panel.add(buttonMr, gbc);
        gbc.gridx = 2;
        gbc.gridy = 1;
        panel.add(buttonMs, gbc);
        gbc.gridx = 3;
        gbc.gridy = 1;
        panel.add(buttonMp, gbc);

        gbc.gridx = 0;
        gbc.gridy = 5;
        panel.add(button1, gbc);
        gbc.gridx = 1;
        gbc.gridy = 5;
        panel.add(button2, gbc);
        gbc.gridx = 2;
        gbc.gridy = 5;
        panel.add(button3, gbc);
        gbc.gridx = 0;
        gbc.gridy = 4;
        panel.add(button4, gbc);
        gbc.gridx = 1;
        gbc.gridy = 4;
        panel.add(button5, gbc);
        gbc.gridx = 2;
        gbc.gridy = 4;
        panel.add(button6, gbc);
        gbc.gridx = 0;
        gbc.gridy = 3;
        panel.add(button7, gbc);
        gbc.gridx = 1;
        gbc.gridy = 3;
        panel.add(button8, gbc);
        gbc.gridx = 2;
        gbc.gridy = 3;
        panel.add(button9, gbc);
        gbc.gridx = 0;
        gbc.gridy = 6;
        panel.add(button0, gbc);

        gbc.gridx = 3;
        gbc.gridy = 2;
        panel.add(buttonMultiply, gbc);
        gbc.gridx = 3;
        gbc.gridy = 3;
        panel.add(buttonDivide, gbc);
        gbc.gridx = 3;
        gbc.gridy = 4;
        panel.add(buttonMinus, gbc);
        gbc.gridx = 3;
        gbc.gridy = 5;
        panel.add(buttonPlus, gbc);
        gbc.gridx = 3;
        gbc.gridy = 6;
        panel.add(buttonEquals, gbc);
        gbc.gridx = 1;
        gbc.gridy = 6;
        panel.add(buttonDot, gbc);
        gbc.gridx = 2;
        gbc.gridy = 6;
        panel.add(buttonToggle, gbc);
        gbc.gridx = 0;
        gbc.gridy = 7;
        panel.add(buttonPI, gbc);
        gbc.gridx = 1;
        gbc.gridy = 7;
        panel.add(buttonExp, gbc);
        gbc.gridx = 2;
        gbc.gridy = 7;
        panel.add(buttonR2, gbc);
        gbc.gridx = 3;
        gbc.gridy = 7;
        panel.add(buttonR0, gbc);
        gbc.gridx = 0;
        gbc.gridy = 2;
        panel.add(buttonClear, gbc);
        gbc.gridx = 1;
        gbc.gridy = 2;
        panel.add(buttonSQRT, gbc);
        gbc.gridx = 2;
        gbc.gridy = 2;
        panel.add(buttonPercent, gbc);
        frame.getContentPane().add(panel, BorderLayout.CENTER);
    }

    //variables
    double operand1 = 0;
    double operand2 = 0;
    double mAns = 0;
    boolean starting = true;
    String operator = "";

    @Override
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();
        switch (command) {
            case "mc" ->
                mAns = 0;
            case "mr" ->
                inputBox.setText(mAns + "");
            case "m-" ->
                mAns -= Double.parseDouble(inputBox.getText());
            case "m+" ->
                mAns += Double.parseDouble(inputBox.getText());
            case "C" ->
                inputBox.setText("");
            case "√" -> {
                operand2 = Math.sqrt(Double.parseDouble(inputBox.getText()));
                inputBox.setText(operand2 + "");
            }
            case "%" ->
                inputBox.setText(Double.parseDouble(inputBox.getText()) / 100 + "");
            case "π" ->
                inputBox.setText("3.1415926536");
            case "+", "-", "x", "/", "^" -> {
                operand1 = Double.parseDouble(inputBox.getText());
                operator = command;
                starting = true;
            }
            case "=" -> {
                if (!starting) {
                    starting = true;
                    operand2 = Double.parseDouble(inputBox.getText());
                }
                inputBox.setText(evaluate(operand1, operand2, operator));
            }
            case "+/-" -> {
                String temp = inputBox.getText();
                if (temp.charAt(0) == '-') {
                    inputBox.setText(temp.substring(1));
                } else {
                    inputBox.setText("-" + temp);
                }
            }
            case "R2" -> {
                inputBox.setText(String.format("%.2f", Double.valueOf(inputBox.getText())));
            }
            case "R0" -> {
                inputBox.setText(String.format("%.0f", Double.valueOf(inputBox.getText())));
            }
            case null, default -> {
                if (starting) {
                    inputBox.setText(command);
                    starting = false;
                } else {
                    inputBox.setText(inputBox.getText() + command);
                }
            }
        }
    }

    public String evaluate(double operand1, double operand2, String operator) {
        switch (operator) {
            case "+" -> {
                this.operand1 = operand1 + operand2;
            }
            case "-" -> {
                this.operand1 = operand1 - operand2;
            }
            case "x" -> {
                this.operand1 = operand1 * operand2;
            }
            case "/" -> {
                this.operand1 = operand1 / operand2;
            }
            case "^" -> {
                this.operand1 = Math.pow(operand1, operand2);
            }
        }
        return this.operand1 + "";
    }
}
