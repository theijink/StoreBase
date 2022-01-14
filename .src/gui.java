//import javax.swing.*;
//import java.awt.*;
//import java.awt.event.*;
import javax.swing.JButton;  
import javax.swing.JFrame;  
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GUI {
    public static void main(String[] args) {  
        // create toplevel container
        JFrame frame=new JFrame();  
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   // close window handler
        frame.setSize(720,480);                                 // set framesize
        //frame.setLayout(null); 

        //////////////// Layout ////////////////
        // |pnl Database actions|
        //   |lbl Database actions|
        //     |btn add item to database|
        //     |btn update items in database|
        //     |btn add code and product name|
        // |pnl Stickers actions|
        //   |lbl Stickers actions|
        //     |btn CCV stickers from .csv file|
        //     |btn BOL stickers from .xls file|
        //     |btn PostNL stickers from .csv file|
        ///////////////////////////////////////////

        // create panel
        JPanel pnl1 = new JPanel();
        frame.add(pnl1);

        // create stickers label
        JLabel lbl1 = new JLabel("Database actions");
        pnl1.add(lbl1);
        //lbl1.setBounds(50, 50, 500, 50);

                        
        // create button DBadd
        JButton btn1 = new JButton("Add item to Database");
        pnl1.add(btn1);                    // add button to frame
        btn1.addActionListener(new LaunchDBadd());
        //btn1.setBounds(50,100, 500,50);      // (x,y,w,h) w.r.t. top left
        
        // create button DBmod
        JButton btn2 = new JButton("Modify item in Database");
        pnl1.add(btn2);
        btn2.addActionListener(new LaunchDBmod());




    }
    
    // create new class for button action LaunchDBadd
    static class LaunchDBadd implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                //System.out.println("Executing java code")
                //create process and execute
                String[] cmd = { "python3", "pygui/gui.py" };
                Process p = Runtime.getRuntime().exec(cmd);
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }
    
    // create new class for button action LaunchDBmod
    static class LaunchDBmod implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                String[] cmd = { "python3", "pygui/gui.py" };
                Process p = Runtime.getRuntime().exec(cmd);
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }


}