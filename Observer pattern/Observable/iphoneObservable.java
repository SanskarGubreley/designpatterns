package Observable;

import java.util.ArrayList;
import java.util.List;

import Observer.NotificationAlertObserver;

public class iphoneObservable implements StocksObservable {
    
    public List<NotificationAlertObserver> objList = new ArrayList<>();
    public int stockCount = 0;

    @Override
    public void add(NotificationAlertObserver obj){
        objList.add(obj);
    }
    @Override
    public void remove(NotificationAlertObserver obj){
        objList.remove(obj);
    }

    @Override
    public void notifySubscribers(){
        for(NotificationAlertObserver observer: objList){
            observer.update();
        }
    }

    public void setStockCount(int newStock){
        if( stockCount == 0){
            notifySubscribers();
        }
        stockCount +=  newStock;
    }
    public int getStockCount(){
        return stockCount;
    }

}
