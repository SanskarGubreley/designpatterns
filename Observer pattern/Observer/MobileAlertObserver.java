package Observer;

import Observable.StocksObservable;


public class MobileAlertObserver implements NotificationAlertObserver {
    String username;
    StocksObservable obj;

    public MobileAlertObserver(String u, StocksObservable o){
        this.username=u;
        this.obj = o;
    }

    @Override
    public void update() {
        sendText(username,"product is in stock hurry up");
    }

    public void sendText(String username,String msg){
        System.out.println("text sent to" + username);
    }
}
