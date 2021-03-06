//import javax.swing.*;
//import java.awt.*;
//import java.awt.event.*;
import javax.swing.JButton;  
import javax.swing.JFrame;  
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.ImageIcon;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Image;

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
        JLabel lbl1 = new JLabel("Database actions:");
        frame.add(lbl1);
        lbl1.setBounds(50, 50, 250, 50);
               
        // create button DBadd
        JButton btn1 = new JButton("Add item to Database");
        frame.add(btn1);                    // add button to frame
        btn1.addActionListener(new LaunchDBadd());
        btn1.setBounds(50,100, 250,50);      // (x,y,w,h) w.r.t. top left
        
        // create button DBmod
        JButton btn2 = new JButton("Modify item in Database");
        frame.add(btn2);
        btn2.addActionListener(new LaunchDBmod());
        btn2.setBounds(50,150, 250,50);

        // create button DBmap
        JButton btn3 = new JButton("Add code-name mapping");
        frame.add(btn3);
        btn3.addActionListener(new LaunchDBmap());
        btn3.setBounds(50,200, 250,50);


        // create stickers label
        JLabel lbl2 = new JLabel("Stickers actions:");
        frame.add(lbl2);
        lbl2.setBounds(50, 250, 250, 50);
               
        // create button DBadd
        JButton btn4 = new JButton("CCV stickers from .csv file");
        frame.add(btn4);                    // add button to frame
        btn4.setEnabled(true);
        btn4.addActionListener(new LaunchPostColumns());
        btn4.setBounds(50,300, 250,50);      // (x,y,w,h) w.r.t. top left
        
        // create button DBmod
        JButton btn5 = new JButton("BOL stickers from .xml file");
        frame.add(btn5);
        btn5.setEnabled(true);
        btn5.addActionListener(new LaunchSelectOrders());
        btn5.setBounds(50,350, 250,50);

        // create button DBmap
        JButton btn6 = new JButton("PostNL stickers from .csv file");
        frame.add(btn6);
        btn6.setEnabled(false);
        btn6.addActionListener(new LaunchDBmap());
        btn6.setBounds(50,400, 250,50);

        frame.setLayout(null);

        // create png image
        ImageIcon img1 = new ImageIcon(new ImageIcon(".bin/statsgraph.png").getImage().getScaledInstance(270, 270, Image.SCALE_DEFAULT));
        JLabel lbl3 = new JLabel(img1);
        frame.add(lbl3);
        lbl3.setBounds(400, 500, 270, 270);

        
    }
    
    // create new class for button action LaunchDBadd
    static class LaunchDBadd implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                //System.out.println("Executing java code")
                //create process and execute
                String[] cmd = { "python3", ".src/StoreBase.py", "DBadd" };
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
                String[] cmd = { "python3", ".src/StoreBase.py", "DBmod" };
                Process p = Runtime.getRuntime().exec(cmd);
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }
    
    // create new class for button action LaunchDBmap
    static class LaunchDBmap implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                String[] cmd = { "python3", ".src/StoreBase.py", "DBmap" };
                Process p = Runtime.getRuntime().exec(cmd);
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

    // create new class for button action LaunchDBmap
    static class LaunchPostColumns implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                String[] cmd = { "python3", ".src/PostColumns.py" };
                Process p = Runtime.getRuntime().exec(cmd);
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

    // create new class for button action LaunchDBmap
    static class LaunchSelectOrders implements ActionListener{
        public void actionPerformed (ActionEvent e){
            try {
                String[] cmd = { "python3", ".src/PostColumns.py" };
                Process p = Runtime.getRuntime().exec(cmd);
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }

}