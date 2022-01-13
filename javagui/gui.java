import javax.swing.JButton;  
import javax.swing.JFrame;  
import java.awt.event.ActionEvent;

public class GUI {
    
    GUI(){  
        // create toplevel container
        JFrame frame=new JFrame();  
                          
        // create button          
        JButton btn1 = new JButton("Add item to Database");
        btn1.setOnAction((new event)
            System.out.println("Button clicked");
        );
        btn1.setBounds(50,50, 150,50);      // (x,y,w,h) w.r.t. top left
        frame.add(btn1);                    // add button to frame



        frame.setSize(720,480);                                 // set framesize
        frame.setLayout(null);  
        frame.setVisible(true);       
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   // close window handler

    }  
              
     public static void main(String[] args) {  
            new GUI();  
     }  
}