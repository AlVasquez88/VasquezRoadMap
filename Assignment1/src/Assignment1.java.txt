import javafx.application.Application;
import javafx.geometry.VPos;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.TextAlignment;
import javafx.stage.Stage;

import java.util.Scanner;

import static javafx.application.Application.launch;

//In the documentation standards,
// I don't know how to create a package for this assignment

//@Author: Alvin Vasquez, 000857238

/**
 * This program inputs data to create a y-axis limit of 2000
 * and a x-axis limit of 100.
 * The program then illustrates the data into a graph.
 * Created: May 21, 2024
 */

public class Assignment1 extends Application {
    public int[] yValues;
    public String[] xLabels;

    public static void main(String[] args) {
        launch(args);
    }


    public void start(Stage stage) throws Exception {
        Group root = new Group();
        Scene scene = new Scene(root);
        Canvas canvas = new Canvas(1000, 800); //Setting canvas
        stage.setTitle("Line Graph"); //Setting window title
        root.getChildren().add(canvas);
        stage.setScene(scene);
        GraphicsContext gc = canvas.getGraphicsContext2D();

        //Inputting Graph Title with Scanner import
        Scanner sin = new Scanner(System.in);
        System.out.print("Enter Title: ");
        String title = sin.nextLine();// new line

        //Establishing boolean
        boolean running = true;

        //Inputting minimum and maximum values for y-axis
        int maxY = 0;
        int maxX = 0;

        //Establihing while loop for inputting and creating sentinel
        while (running) {
            System.out.println("Enter Option [START, QUIT]");
            String option = sin.next();
            option = option.toUpperCase();
            sin.nextLine();

            if (option.equals("START")) {
                int yAxis;
                System.out.print("Please enter maximum value of the Y-Axis ( > 0): ");
                yAxis = sin.nextInt();

                //If users input y axis less than 0
                while (yAxis < 0) {
                    System.out.println("Input is out of range - must be > 0");
                    System.out.print("Please enter maximum value of the Y-Axis ( > 0): ");
                    yAxis = sin.nextInt();
                }
                //If users input y axis that is greater than 2000
                while (yAxis >= 2001) {
                    System.out.println("Input is out of range - must be <= 2000");
                    System.out.print("Please enter maximum value of the Y-Axis ( > 0): ");
                    yAxis = sin.nextInt();
                }
                maxY = yAxis;

                //Establishing input for x-axis
                int xAxis;
                System.out.println("Enter the number of items to graph (1-100): ");
                xAxis = sin.nextInt();

                //If users input items less than 0
                while (xAxis < 0) {
                    System.out.println("Input is out of range - must be > 0");
                    System.out.print("Please enter the number of items to graph (1-100): ");
                    xAxis = sin.nextInt();
                }
                //If users input items that is equal or greater than 101
                while (xAxis >= 101) {
                    System.out.println("Input is out of range - must be <= 101");
                    System.out.print("Please enter the number of items to graph (1-100): ");
                    xAxis = sin.nextInt();
                }

                maxX = xAxis;

                //Defining arrays for x labels and y values
                xLabels = new String[maxX];
                yValues = new int[maxX];

                //inputting series for x variable
                for (int i = 0; i < maxX; i++) {
                    System.out.println("Enter the series name for Label " + (i + 1) + ": ");
                    xLabels[i] = sin.next();

                    System.out.print("Enter value for " + xLabels[i] + ": ");
                    yValues[i] = sin.nextInt();

                    //If users input numbers less than 0 or greater than maxY variable
                    while (yValues[i] < 0 || yValues[i] > maxY) {
                        System.out.println("Input is out of range - must be greater than 0 and less than the range of the y axis.");
                        System.out.println("Enter value for " + xLabels + ": ");
                        yValues[i] = sin.nextInt();

                    }
                }//Creating sentinel
            } else if (option.equals("QUIT")) {
                running = false;
            } else {
                System.out.println("Invalid option. Please enter START or QUIT.");
            }
        }
        System.out.println("Establishing Graph...");


        //Background Color Illustration
        gc.setFill(Color.BLACK);
        gc.fillRect(0, 0, 1000, 800);
        gc.setStroke(Color.WHITE);

        //Font Illustration
        Font f = new Font("Sans-Serif", 72);
        gc.setFont(f);
        gc.setTextAlign(TextAlignment.CENTER);
        gc.setTextBaseline(VPos.CENTER);
        gc.setFill(Color.CRIMSON);
        gc.fillText(title, 500, 50);
        gc.setStroke(Color.rgb(200, 180, 0));
        gc.setLineDashes(6, 4);
        gc.strokeText(title, 500, 50);
        gc.setLineDashes(null); //removing dashes for other drawings

        //Axis illustration
        drawAxes(gc,maxY,maxX);

        //Draw Grid
        drawGrid(gc, maxY, maxX);

        //Plotting data points and connect with lines
        plotData(gc, yValues, xLabels, maxY, maxX);

        stage.show();
    }
    public void drawAxes(GraphicsContext gc, int maxY, int maxX){
        gc.setStroke(Color.WHITE);
        gc. setLineWidth(2);

        //Y-Axis
        gc.strokeLine(100,700,100,100);
        //X-Axis
        gc.strokeLine(100,700,900,700);

        //Y-Axis Labels
        gc.setTextAlign(TextAlignment.RIGHT);
        gc.setTextBaseline(VPos.CENTER);
        gc.setFont(new Font("Sans-Serif", 20));
        gc.strokeText("0",90,700);
        gc.strokeText(String.valueOf(maxY),90,100);
        gc.strokeText(String.valueOf(maxY / 2), 90, 400);

        //X-Axis Labels
        gc.setTextAlign(TextAlignment.CENTER);
        for (int i = 0; i < maxX; i++) {
            int x = 100 + (i * (800 / (maxX - 1)));
            gc.strokeText(String.valueOf(i + 1), x, 720);
        }
    }
    public void drawGrid(GraphicsContext gc, int maxY, int maxX) {
        gc.setStroke(Color.GRAY);
        gc.setLineWidth(1);

        //Drawing horizontal grid lines
        for (int i = 1; i <= 10; i++) {
            int y = 700 - (i * 60);
            gc.strokeLine(100, y, 900, y);
        }
        //Drawing vertical grid lines
        for (int i = 0; i < maxX; i++){
            int x = 100 + (i * (800 / (maxX - 1)));
            gc.strokeLine(x, 700, x, 100);
        }
    }
    public void plotData(GraphicsContext gc, int[] yValues, String[] xLabels, int maxY, int maxX){
        gc.setStroke(Color.PAPAYAWHIP);
        gc.setLineWidth(2);

        int prevX = 100;
        int prevY = 700;

        for (int i = 0; i < maxX; i++){
            int x = 100 + (i * (800 / (maxX - 1)));
            int y = 700 - (int)((yValues[i] / (double) maxY) * 600);

            //Draw Line
            if (i > 0){
                gc.strokeLine(prevX, prevY, x, y);
            }
            //Draw Point
            gc.fillOval(x - 3, y - 3, 6, 6);

            //Draw Label
            gc.setFill(Color.WHITE);
            gc.setTextAlign(TextAlignment.CENTER);
            gc.setFont(new Font("Sans-Serif", 14));
            gc.fillText(xLabels[i], x, y, - 10);

            prevX = x;
            prevY = y;
        }

    }
}