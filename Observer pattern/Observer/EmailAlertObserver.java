package Observer;

import Observable.StocksObservable;


public class EmailAlertObserver implements NotificationAlertObserver {
    String emailid;
    StocksObservable observable;

    public EmailAlertObserver(String emailid , StocksObservable obj){
        this.emailid = emailid;
        this.observable = obj;
    }

    @Override
    public void update(){
        sendMail(emailid, "heyy");
    }

    public void sendMail(String emailid,String msg){
        System.out.println("mail sent to "+ emailid);
    }
}
